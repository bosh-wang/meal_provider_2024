from flask import Flask, request, jsonify, make_response
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    return psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
    )

def create_order(data):
    # data = request.json
    user_id = data.get('user_id')
    restaurant_id = data.get('restaurant_id')
    items = data.get('items')  # List of items, each item is a dict with item_id and quantity

    if not (user_id and restaurant_id and items):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Create new order
        cursor.execute("INSERT INTO orders (user_id, restaurant_id, order_status) VALUES (%s, %s, %s) RETURNING order_id, order_date", 
                       (user_id, restaurant_id, 'PENDING'))
        new_order = cursor.fetchone()
        order_id = new_order['order_id']
        order_date = new_order['order_date']

        # Insert items into orders_items and calculate total_price
        total_price = 0
        for item in items:
            item_id = item['item_id']
            quantity = item['quantity']
            
            cursor.execute("SELECT price FROM menus_items WHERE item_id = %s", (item_id,))
            item_price = cursor.fetchone()['price']
            
            cursor.execute("INSERT INTO orders_items (order_id, item_id, quantity, price) VALUES (%s, %s, %s, %s)",
                           (order_id, item_id, quantity, item_price))
            
            total_price += item_price * quantity
        
        # Update total_price in orders table
        cursor.execute("UPDATE orders SET total_price = %s WHERE order_id = %s", (total_price, order_id))
        
        conn.commit()
        cursor.close()
        conn.close()

        response = jsonify({
            "order_id": order_id,
            "user_id": user_id,
            "restaurant_id": restaurant_id,
            "order_status": "PENDING",
            "total_price": total_price,
            "order_date": order_date,
            "items": items
        })
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return make_response(response, 201)
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

# @app.route('/change_order_status', methods=['POST'])
def change_order_status(data):
    # data = request.json
    order_id = data.get('order_id')
    order_status_before = data.get('order_status_before')
    order_status_after = data.get('order_status_after')

    if not (order_id and order_status_before and order_status_after):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    if order_status_before == 'PENDING' and order_status_after == 'CONFIRMED':
        new_order_status = 'CONFIRMED'
    elif order_status_before == 'CONFIRMED' and order_status_after == 'PREPARED':
        new_order_status = 'PREPARED'
    elif order_status_before == 'PREPARED' and order_status_after == 'COMPLETED':
        new_order_status = 'COMPLETED'
    elif order_status_before!='COMPLETED' and order_status_after == 'CANCELED':
        new_order_status = 'CANCELED'
    else:
        return make_response(jsonify({"error": "Invalid order status transition"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE orders SET order_status = %s WHERE order_id = %s AND order_status = %s", 
                       (new_order_status, order_id, order_status_before))
        if cursor.rowcount == 1:
            conn.commit()
            cursor.close()
            conn.close()
            return make_response(jsonify({"message": "Order status changed successfully"}), 200)
        else:
            return make_response(jsonify({"error": "Invalid order ID or order status"}), 404)
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)


def get_order(data):
    order_id = data.get('order_id')

    if not order_id:
        return make_response(jsonify({"error": "Missing order_id parameter"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Fetch order details
        cursor.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
        order_data = cursor.fetchone()

        if not order_data:
            return make_response(jsonify({"error": "Order not found"}), 404)
        
        # Fetch order items
        cursor.execute("SELECT item_id, quantity, price FROM orders_items WHERE order_id = %s", (order_id,))
        items_data = cursor.fetchall()

        response = jsonify({
            "order_id": order_data['order_id'],
            "user_id": order_data['user_id'],
            "restaurant_id": order_data['restaurant_id'],
            "order_status": order_data['order_status'],
            "total_price": order_data['total_price'],
            "order_date": order_data['order_date'],
            "items": items_data
        })
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return make_response(response, 200)
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    finally:
        cursor.close()
        conn.close()