from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
import pandas as pd
app = Flask(__name__) # Here we are creating an instance of the Flask app.


"""
Below, you will see the `restaurants` list, which contains a few dictionaries.
Each dictionary within the `restaurants` list has a name and a list of items,
where each item is a dictionary with a name and a price.
"""

# restaurants = [
#     {
#         "name": "Tasty Burgers",
#         "items": [
#             {
#                 "name": "Classic Burger",
#                 "price": 8.99
#             },
#             {
#                 "name": "Cheeseburger",
#                 "price": 9.99
#             }
#         ]
#     },
#     {
#         "name": "Pizza Palace",
#         "items": [
#             {
#                 "name": "Pepperoni Pizza",
#                 "price": 11.99
#             },
#             {
#                 "name": "Margherita Pizza",
#                 "price": 10.99
#             }
#         ]
#     }
# ]

# fast_food = {
#     "Restaurant": ["Tasty Burgers","Tasty Burgers", "Pizza Palace", "Pizza Palace"],
#     "Items": ["Classic Burger","Cheeseburger", "Pepperoni Pizza", "Margherita Pizza"],
#     "Price": [8.99,9.99, 11.99, 10.99]
# }
# df = pd.DataFrame(fast_food)
# # print(df)
# restaurants = []
# for name, group in df.groupby("Restaurant"):
#     items = [{"name": row["Items"], "price": row["Price"]} for idx, row in group.iterrows()]
#     restaurants.append({"name": name, "items": items})
# print(restaurants)

import psycopg2
from config import load_config
from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
import pandas as pd
app = Flask(__name__) # Here we are creating an instance of the Flask app.

# 取得config內的資訊
config = load_config()
Database = config['GCP']['database']
Host = config['GCP']['host']
User = config['GCP']['user']
Password = config['GCP']['password']
Port = config['GCP']['port']
# 連線
conn = psycopg2.connect(database=Database,
                        host=Host,
                        user=User,
                        password=Password,
                        port=Port)

# 從資料庫取資料
conn.set_client_encoding('UTF8')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM restaurants")
size = cursor.fetchone()
print(size[0])
cursor.execute("SELECT * FROM menus_items;")
data = cursor.fetchmany(size=size[0])

conn.close()
print(data)
# 定义列名
columns = ['item_id', 'menu_id', 'restaurant_id', 'category', 'item_name', 'description', 'price', 'available', 'image', 'image_url', 'created_time']
# 创建 DataFrame
df = pd.DataFrame(data, columns=columns)
df = df.head(3)
# 打印 DataFrame
print(df)

json_result = df.to_json(orient="records",force_ascii=False)
print(json_result)

@app.get("/menu")
# The above is a decorator that defines a route for handling GET requests
# to the `/restaurant` endpoint.

def get_menu():
    response = jsonify({"menu": menu})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response
    # return {"menu": data}
# The above is a function that returns a dictionary that contains the `restaurants` list



