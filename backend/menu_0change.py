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
# fast_food = {
#     "Restaurant": ["Tasty Burgers","Tasty Burgers", "Pizza Palace", "Pizza Palace"],
#     "Items": ["Classic Burger","Cheeseburger", "Pepperoni Pizza", "Margherita Pizza"],
#     "Price": [8.99,9.99, 11.99, 10.99]
# }
# df_menu = pd.DataFrame(fast_food)

# 读取 order.json 文件并解析数据
with open('adjust_menu.json', 'r') as f:
    adj_data = json.load(f)
# 解析 order.json 中的数据
add_del = adj_data['change_status']
Restaurant = adj_data['restaurant_id']
Item = adj_data['items'][0]['name']
price = adj_data['items'][0]['price']

cursor = conn.cursor()
if add_del == 'ADD':
    # 構建 SQL 語句
    insert_query = """
    INSERT INTO menus_items (item_id, menu_id, restaurant_id, category,item_name,description,price,availability,image,image_url)
    VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s)
    RETURNING order_id;
    """
    # 執行 SQL 語句
    cursor.execute(insert_query, ('item041', 'menu02',Restaurant, "主食",Item,"goooooood",price,True,None,r"https://storage.googleapis.com/meal_provider_system/%E8%B1%AC%E8%A1%80%E7%B3%95.jpg"))
elif add_del == 'DELETE':
    for index, row in df_menu.iterrows():
        if row['Restaurant'] == Restaurant and row['Items'] == Item:
            ind = index
    df_menu = df_menu.drop(index = ind)
else: #add_del == 'ADJUST':
    for index, row in df_menu.iterrows():
        if row['Restaurant'] == Restaurant and row['Items'] == Item:
            ind = index
            print(ind)
    df_menu.loc[ind,'Price'] = price
# print(df_menu)
# restaurants = []
# for name, group in df_menu.groupby("Restaurant"):
#     items = [{"name": row["Items"], "price": row["Price"]} for idx, row in group.iterrows()]
#     restaurants.append({"name": name, "items": items})
# print(restaurants)
conn.close()
