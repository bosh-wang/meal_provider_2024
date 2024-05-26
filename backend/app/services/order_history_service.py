from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_order_history_service(data):
    
    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d").strftime('%a, %d %b %Y %H:%M:%S GMT')
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d").strftime('%a, %d %b %Y %H:%M:%S GMT')
        customer_id = data['customer_id']

        cursor.execute('''SELECT 
                       orders.user_id, 
                       orders.order_date,
                       orders.total_price FROM 
                       orders WHERE 
                       orders.customer_id = %s AND 
                       orders.order_date BETWEEN %s AND %s''', (customer_id, start_date, end_date))
        orders = cursor.fetchall()

        order_history = []
        for order_id, order_date, total_price in orders:
            cursor.execute('''SELECT 
                           item_id, 
                           quantity, 
                           unit_price FROM 
                           orders_items WHERE 
                           order_id = %s''', order_id)
            items = cursor.fetchall()
            item_list = []
            for item_id, quantity, unit_price in items:
                cursor.execute("SELECT item_name FROM menus_items WHERE item_id = %s", item_id)
                item_name = cursor.fetchall()
                item_list.append({
                    "item_id": item_id,
                    "item_name": item_name,
                    "quantity": quantity,
                    "unit_price": unit_price
                })
            order_history.append({
                "order_id": order_id,
                "order_date": order_date.strftime('%Y-%m-%dT%H:%M:%S'),
                "items": item_list,
                "total_price": total_price
            })

        cursor.close()
        conn.close()
        return ({"orders": order_history})
    except Exception as e:
        return ({"error": str(e)}), 500

def test(data1):

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:

        cursor.execute("SELECT * FROM meals_ratings")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return ({"data": data, "request": data1})
    except Exception as e:
        return ({"error": str(e)}), 500