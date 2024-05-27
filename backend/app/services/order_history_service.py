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
        start_date = str(datetime.strptime(data['start_date'], "%Y-%m-%d"))#.strftime('%a, %d %b %Y %H:%M:%S GMT'))
        end_date = str(datetime.strptime(data['end_date'], "%Y-%m-%d"))#.strftime('%a, %d %b %Y %H:%M:%S GMT'))
        customer_id = data['customer_id']

        query = '''SELECT 
                       orders.order_id,
                       orders.order_date,
                       orders.total_price FROM 
                       orders WHERE 
                       orders.user_id = %s AND 
                       orders.order_date BETWEEN %s AND %s;'''
        cursor.execute(query, (customer_id, start_date, end_date,))
        orders = cursor.fetchall()

        order_history = []
        for order_id, order_date, total_price in orders:
            cursor.execute('''SELECT 
                           item_id, 
                           quantity, 
                           price FROM 
                           orders_items WHERE 
                           order_id = %s''', (order_id,))
            items = cursor.fetchall()
            item_list = []
            for item_id, quantity, item_total_price in items:
                cursor.execute("SELECT item_name FROM menus_items WHERE item_id = %s", (item_id,))
                item_name = cursor.fetchall()
                item_list.append({
                    "item_id": item_id,
                    "item_name": item_name,
                    "quantity": quantity,
                    "unit_price": item_total_price/quantity
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

def test():

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

        # cursor.execute('DELETE FROM meals_ratings WHERE rating_id = %s;' ,("0",))
        cursor.execute('SELECT * FROM orders')
        data = cursor.fetchall()
        # conn.commit()
        cursor.close()
        conn.close()
        return ({"data": data})
    except Exception as e:
        return ({"error": str(e)}), 500