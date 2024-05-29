from flask import Flask, request, jsonify, make_response
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import pytz
import json
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

def change_menu_item():
    data = request.json
    change_status = data.get('change_status')

    if change_status == 'ADD':
        return add_menu_item(data)
    elif change_status == 'ADJUST':
        return adjust_menu_item(data)
    elif change_status == 'DELETE':
        return delete_menu_item(data)
    else:
        return make_response(jsonify({"error": "Invalid change_status"}), 400)

def add_menu_item(data):
    restaurant_id = data.get('restaurant_id')
    category = data.get('category')
    item_name = data.get('item_name')
    description = data.get('description')
    price = data.get('price')
    availability = data.get('availability')
    image_url = data.get('image_url')

    if not (restaurant_id and category and item_name and description and price and availability and image_url):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # 获取当前最后一项的 item_id
        cursor.execute("SELECT item_id FROM menus_items ORDER BY item_id DESC LIMIT 1")
        last_item_id = cursor.fetchone()
        if last_item_id:
            last_item_id = last_item_id['item_id']
            last_index = int(last_item_id.split('item')[-1])
            new_item_id = f'item{last_index + 1:03d}'
        else:
            new_item_id = 'item001'  # 如果database为空，则从第一项开始
        menu_id = 'menu01'
        image = None
        created_time = datetime.now(pytz.timezone('Asia/Taipei')).isoformat()

        insert_query = """
        INSERT INTO menus_items (
            item_id, menu_id, restaurant_id, category, item_name, 
            description, price, availability, image, image_url, created_time
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            new_item_id, menu_id, restaurant_id, category, item_name, 
            description, price, availability, image, image_url, created_time
        ))
        
        conn.commit()
        cursor.close()
        conn.close()
        response_data = {
            "item_id": new_item_id,
            "menu_id": menu_id,
            "restaurant_id": restaurant_id,
            "category": category,
            "item_name": item_name,
            "description": description,
            "price": price,
            "availability": availability,
            "image": image,
            "image_url": image_url,
            "created_time": created_time
        }

        response_json = json.dumps(response_data, ensure_ascii=False)
        response = make_response(response_json, 201)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

def adjust_menu_item(data):
    item_name = data.get('item_name')
    new_price = data.get('price')

    if not (item_name and new_price):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        update_query = """
        UPDATE menus_items
        SET price = %s
        WHERE item_name = %s
        RETURNING item_id, item_name, price
        """

        cursor.execute(update_query, (new_price, item_name))
        updated_item = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if updated_item:
            response_data = {
                "item_id": updated_item['item_id'],
                "item_name": updated_item['item_name'],
                "price": updated_item['price'],
                "message": "Price updated successfully"
            }

            response_json = json.dumps(response_data, ensure_ascii=False)
            response = make_response(response_json, 201)
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return response
        else:
            return make_response(jsonify({"error": "Item not found"}), 404)
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

def delete_menu_item(data):
    item_name = data.get('item_name')

    if not item_name:
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        delete_query = """
            UPDATE menus_items
            SET availability = FALSE
            WHERE item_name = %s
            RETURNING item_id;
            """

        cursor.execute(delete_query, (item_name,))
        deleted_item = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if deleted_item:
            return make_response(jsonify({"message": "Item deleted successfully"}), 200)
        else:
            return make_response(jsonify({"error": "Item not found"}), 404)
    
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)