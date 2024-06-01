import psycopg2
from config import load_config
from flask import (
    Flask,
)  # Here we are importing the Flask class. This class is used to create the app.
import pandas as pd

app = Flask(__name__)  # Here we are creating an instance of the Flask app.

# 取得config內的資訊
config = load_config()
Database = config["GCP"]["database"]
Host = config["GCP"]["host"]
User = config["GCP"]["user"]
Password = config["GCP"]["password"]
Port = config["GCP"]["port"]
# 連線
conn = psycopg2.connect(
    database=Database, host=Host, user=User, password=Password, port=Port
)

# 從資料庫取資料
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM restaurants")
size = cursor.fetchone()
print(size[0])
cursor.execute("SELECT * FROM menus_items;")
data = cursor.fetchmany(size=size[0])
conn.close()
# 定义列名
columns = [
    "item_id",
    "menu_id",
    "restaurant_id",
    "category",
    "item_name",
    "description",
    "price",
    "available",
    "image",
    "image_url",
    "created_time",
]
# 创建 DataFrame
df = pd.DataFrame(data, columns=columns)

# 打印 DataFrame
print(df)

json_result = df.to_json(orient="records", date_format="iso", force_ascii=False)
print(json_result)


@app.get("/menu")
def get_menu():
    return {"menu": json_result}


# conn = psycopg2.connect(database="postgres",
#                         host="localhost",
#                         user="backend",
#                         password="backend",
#                         port=5432)

# restaurants有四十筆
# cursor.execute("SELECT COUNT(*) FROM restaurants")

# names = [n[0] for n in name]
# print(names)
# print(cursor.fetchmany(size=3))
