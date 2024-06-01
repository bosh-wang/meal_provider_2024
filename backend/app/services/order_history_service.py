from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os

# load_dotenv()

def get_order_history_service_for_employee(data):
    
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
                       orders.order_status, 
                       orders.paid,
                       orders.total_price FROM 
                       orders WHERE 
                       orders.user_id = %s AND 
                       orders.order_date BETWEEN %s AND %s;'''
        cursor.execute(query, (customer_id, start_date, end_date,))
        orders = cursor.fetchall()

        order_history = []
        for order_id, order_date, order_status, paid, total_price in orders:
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
                "total_price": total_price, 
                "order_status": order_status,
                "paid": paid
            })

        cursor.close()
        conn.close()
        return ({"orders": order_history})
    except Exception as e:
        return ({"error": str(e)}), 500

def get_order_history_service_for_hr(data):
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

        query = '''SELECT 
                       orders.user_id,
                       orders.order_id,
                       orders.order_date,
                       orders.total_price,
                       orders.paid FROM 
                       orders WHERE 
                       orders.order_date BETWEEN %s AND %s;'''
        cursor.execute(query, (start_date, end_date,))
        orders = cursor.fetchall()

        order_history = []
        for user_id, order_id, order_date, total_price, paid in orders:
            if user_id == "user01":
                continue
            cursor.execute('''SELECT
                            employees.department, 
                            employees.position FROM
                            employees WHERE
                            employees.user_id = %s;''', (user_id,))
            employee_info = cursor.fetchall()
            
            department, position = employee_info[0][0], employee_info[0][1]

            order_history.append({
                "customer_id": user_id,
                "department": department,
                "position": position,
                "order_id": order_id,
                "order_date": order_date.strftime('%Y-%m-%dT%H:%M:%S'),
                "total_price": total_price, 
                "paid": paid
            })

        cursor.close()
        conn.close()
        return ({"orders": order_history})
    except Exception as e:
        return ({"error": str(e)}), 500

def get_order_history_service_for_restaurant(data):
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
        restaurant_id = data['restaurant_id']

        query = '''SELECT 
                       orders.order_id,
                       orders.user_id,
                       orders.order_date,
                       orders.confirmed_date, 
                       orders.prepared_date,
                       orders.completed_date,
                       orders.canceled_date,
                       orders.total_price, 
                       orders.order_status, 
                       orders.paid FROM 
                       orders WHERE 
                       orders.restaurant_id = %s AND 
                       orders.order_date BETWEEN %s AND %s;'''
        cursor.execute(query, (restaurant_id, start_date, end_date,))
        orders = cursor.fetchall()

        order_history = []
        for order_id, user_id, order_date, confirmed_date, prepared_date, completed_date, canceled_date, total_price, order_status, paid in orders:
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
                "customer_id": user_id,
                "order_id": order_id,
                "order_date": order_date.strftime('%Y-%m-%dT%H:%M:%S') if order_date else None,
                "confirmed_date": confirmed_date.strftime('%Y-%m-%dT%H:%M:%S') if confirmed_date else None,
                "prepared_date": prepared_date.strftime('%Y-%m-%dT%H:%M:%S') if prepared_date else None,
                "completed_date": completed_date.strftime('%Y-%m-%dT%H:%M:%S') if completed_date else None,
                "canceled_date": canceled_date.strftime('%Y-%m-%dT%H:%M:%S') if canceled_date else None,
                "items": item_list,
                "order_status": order_status,
                "total_price": total_price,
                "paid": paid
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
        cursor.execute('SELECT * FROM employees')
        data = cursor.fetchall()
        # conn.commit()
        cursor.close()
        conn.close()
        return ({"data": data})
    except Exception as e:
        return ({"error": str(e)}), 500
=======
load_dotenv()


def get_order_history_service():  # data
    # host = os.getenv("DB_HOST")
    # dbname = os.getenv("DB_NAME")
    # user = os.getenv("DB_USER")
    # password = os.getenv("DB_PASSWORD")
    # sslmode = "require"
    # conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    # conn = psycopg2.connect(conn_string)
    # print("Connection established")
    # cursor = conn.cursor()

    # try:
    #     start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    #     end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    #     customer_id = data['customer_id']

    #     cursor.execute("SELECT orders.order_id, orders.order_date, orders.total_price FROM orders WHERE orders.customer_id = %s AND orders.order_date BETWEEN %s AND %s", (customer_id, start_date, end_date))
    #     orders = cursor.fetchall()

    #     order_history = []
    #     for order in orders:
    #         order_id, order_date, total_price = order
    #         cursor.execute("SELECT item_id, item_name, quantity, unit_price FROM order_items WHERE order_id = %s", order_id)
    #         items = cursor.fetchall()
    #         item_list = []
    #         for item in items:
    #             item_id, item_name, quantity, unit_price = item
    #             item_list.append({
    #                 "product_id": item_id,
    #                 "name": item_name,
    #                 "quantity": quantity,
    #                 "unit_price": float(unit_price)
    #             })
    #         order_history.append({
    #             "order_id": order_id,
    #             "order_date": order_date.strftime('%Y-%m-%dT%H:%M:%S'),
    #             "items": item_list,
    #             "total_amount": float(total_price)
    #         })

    # cursor.close()
    # conn.close()
    #     return ({"orders": order_history})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return {
        "orders": [
            {
                "order_id": "123456",
                "order_date": "2024-04-15 10:30:00",
                "items": [
                    {
                        "item_id": "ABC123",
                        "item_name": "Spaghetti Carbonara",
                        "quantity": 2,
                        "unit_price": 12.99,
                    },
                    {
                        "item_id": "DEF456",
                        "item_name": "Caesar Salad",
                        "quantity": 1,
                        "unit_price": 8.99,
                    },
                ],
                "total_price": 34.97,
            },
            {
                "order_id": "789012",
                "order_date": "2024-04-20T12:00:00",
                "items": [
                    {
                        "item_id": "GHI789",
                        "item_name": "Margherita Pizza",
                        "quantity": 1,
                        "unit_price": 14.99,
                    }
                ],
                "total_price": 14.99,
            },
        ]
    }