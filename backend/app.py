from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from config import load_config
import json
from decimal import Decimal
from datetime import datetime, date

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    config = load_config()
    conn = psycopg2.connect(
        database=config['GCP']['database'],
        host=config['GCP']['host'],
        user=config['GCP']['user'],
        password=config['GCP']['password'],
        port=config['GCP']['port']
    )
    conn.set_client_encoding('UTF8')
    return conn

def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

@app.route('/menu', methods=['GET'])
def get_menu():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            SELECT 
                m.item_id,
                m.restaurant_id,
                m.category,
                m.item_name,
                m.description,
                m.price,
                m.availability,
                m.image_url,
                ROUND(AVG(r.star_rating), 1) AS star_rating
            FROM 
                menus_items m
            LEFT JOIN 
                meals_ratings r ON m.item_id = r.item_id
            GROUP BY 
                m.item_id,
                m.restaurant_id,
                m.category,
                m.item_name,
                m.description,
                m.price,
                m.availability,
                m.image_url
            ORDER BY 
                m.item_id;
        """
        
        cursor.execute(query)
        menu_items = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        # Convert the results to a JSON string with ensure_ascii=False
        json_result = json.dumps(menu_items, ensure_ascii=False, default=custom_json_serializer)
        
        response = app.response_class(
            response=json_result,
            status=200,
            mimetype='application/json'
        )
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, jsonify
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from config import load_config
# import pandas as pd
# import json
# from datetime import datetime

# app = Flask(__name__)

# # Database connection configuration
# def get_db_connection():
#     config = load_config()
#     conn = psycopg2.connect(
#         database=config['GCP']['database'],
#         host=config['GCP']['host'],
#         user=config['GCP']['user'],
#         password=config['GCP']['password'],
#         port=config['GCP']['port']
#     )
#     conn.set_client_encoding('UTF8')
#     return conn

# def custom_json_serializer(obj):
#     if isinstance(obj, datetime):
#         return obj.isoformat()
#     raise TypeError("Type not serializable")

# @app.route('/menu', methods=['GET'])
# def get_menu():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=RealDictCursor)
        
#         query = """
#         SELECT 
#             m.*,
#             ROUND(AVG(r.star_rating), 1) AS star_rating
#         FROM 
#             menus_items m
#         LEFT JOIN 
#             meals_ratings r ON m.item_id = r.item_id
#         GROUP BY 
#             m.item_id,
#             m.menu_id,
#             m.restaurant_id,
#             m.category,
#             m.item_name,
#             m.description,
#             m.price,
#             m.availability,
#             m.image,
#             m.image_url;
#         """
        
#         cursor.execute(query)
#         menu_items = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         json_result = json.dumps(menu_items, ensure_ascii=False, default=custom_json_serializer)
#         response = app.response_class(
#             response=json_result,
#             status=200,
#             mimetype='application/json'
#         )
        
#         # response = jsonify({"menu": json_result})
#         response.headers['Content-Type'] = 'application/json; charset=utf-8'
#         return response
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

#以上為今天在處理時間序列問題的版本




# from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
# import pandas as pd
# app = Flask(__name__) # Here we are creating an instance of the Flask app.


# """
# Below, you will see the `restaurants` list, which contains a few dictionaries.
# Each dictionary within the `restaurants` list has a name and a list of items,
# where each item is a dictionary with a name and a price.
# """

# import psycopg2
# from config import load_config
# from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
# import pandas as pd
# app = Flask(__name__) # Here we are creating an instance of the Flask app.

# # 取得config內的資訊
# config = load_config()
# Database = config['GCP']['database']
# Host = config['GCP']['host']
# User = config['GCP']['user']
# Password = config['GCP']['password']
# Port = config['GCP']['port']
# # 連線
# conn = psycopg2.connect(database=Database,
#                         host=Host,
#                         user=User,
#                         password=Password,
#                         port=Port)

# # 從資料庫取資料
# conn.set_client_encoding('UTF8')
# cursor = conn.cursor()
# cursor.execute("SELECT COUNT(*) FROM menus_items")
# size = cursor.fetchone()
# print(size[0])
# cursor.execute("SELECT * FROM menus_items;")
# data = cursor.fetchmany(size=1)

# conn.close()
# print(data)
# # 定义列名
# columns = ['item_id', 'menu_id', 'restaurant_id', 'category', 'item_name', 'description', 'price', 'available', 'image', 'image_url', 'created_time']
# # 创建 DataFrame
# df = pd.DataFrame(data, columns=columns)
# df = df.head(3)
# # 打印 DataFrame
# print(df)

# json_result = df.to_json(orient="records",force_ascii=False)
# print(json_result)

# @app.get("/menu")
# # The above is a decorator that defines a route for handling GET requests
# # to the `/restaurant` endpoint.

# def get_menu():
#     # response = jsonify({"menu": menu})
#     # response.headers['Content-Type'] = 'application/json; charset=utf-8'
#     # return response
#     return {"menu": data}


# # 以上可以取出要的值和rating
# SELECT 
#     m.*,
#     ROUND(AVG(r.star_rating), 1) AS star_rating
# FROM 
#     menu_items m
# LEFT JOIN 
#     meals_ratings r ON m.item_id = r.item_id
# GROUP BY 
#     m.item_id,
#     m.menu_id,
#     m.restaurant_id,
#     m.category,
#     m.item_name,
#     m.description,
#     m.price,
#     m.availability,
#     m.image,
#     m.image_url;