from datetime import datetime
import mysql.connector


def get_order_history_service():#data
    
    # conn = mysql.connector.connect(
    # host='localhost',           
    # user='user',               
    # password='@MySQLPassword', 
    # )
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

    #     cursor.close()
    #     return ({"orders": order_history})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return ({
        "orders": [
            {
            "order_id": "123456",
            "order_date": "2024-04-15 10:30:00",
            "items": [
                {
                "item_id": "ABC123",
                "item_name": "Spaghetti Carbonara",
                "quantity": 2,
                "unit_price": 12.99
                },
                {
                "item_id": "DEF456",
                "item_name": "Caesar Salad",
                "quantity": 1,
                "unit_price": 8.99
                }
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
                "unit_price": 14.99
                }
            ],
            "total_price": 14.99,
            }
        ]
        }
    )
