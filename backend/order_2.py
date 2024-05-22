import psycopg2
from config import load_config
from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
import pandas as pd
import json
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

# 從json檔案取資料
orders_df = pd.DataFrame(data)
print(orders_df)

# 读取 order.json 文件并解析数据
with open('order.json', 'r') as f:
    order_data = json.load(f)

# 解析 order.json 中的数据
customer_ID = order_data['customer_ID']
restaurant = order_data['restaurant']
order_items = order_data['items']
quantity = order_data['quantity']
# 仅提取项目名称
item_names = ', '.join(item['name'] for item in order_items)
total_price = sum(item['price'] for item in order_items)



# 寫進database
# 插入数据的 SQL 语句
insert_query = """
INSERT INTO orders (restaurant, customer_ID, order_items, quantity)
VALUES (%s, %s, %s, %s);
"""
cursor = conn.cursor()
# 执行插入数据的 SQL 语句
cur.execute(insert_query, (restaurant, customer_ID, order_items, quantity))
# cursor.execute("SELECT COUNT(*) FROM restaurants")
# size = cursor.fetchone()
# print(size[0])
# cursor.execute("SELECT * FROM menus_items;")
# data = cursor.fetchmany(size=size[0])
conn.close()
