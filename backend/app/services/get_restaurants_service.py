# from flask import Flask, jsonify
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import json
# from decimal import Decimal
# from datetime import datetime, date
# import os

# app = Flask(__name__)

# # Database connection configuration
# def get_db_connection():
#     conn = psycopg2.connect(
#         host = os.getenv("DB_HOST"),
#         database = os.getenv("DB_NAME"),
#         user = os.getenv("DB_USER"),
#         password = os.getenv("DB_PASSWORD"),
#         port = os.getenv("DB_PORT")
#     )
#     conn.set_client_encoding('UTF8')
#     return conn

# def custom_json_serializer(obj):
#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     elif isinstance(obj, Decimal):
#         return float(obj)
#     raise TypeError(f"Type {type(obj)} not serializable")


# def get_restaurant():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=RealDictCursor)
        
#         query = """
#             SELECT 
#                 r.restaurant_id,
#                 r.type AS restaurant_type,
#                 r.name AS restaurant_name,
#                 r.image_url
#             FROM 
#                 restaurants r
#             ORDER BY 
#                 r.restaurant_id;
#         """
        
#         cursor.execute(query)
#         menu_items = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         # Convert the results to a JSON string with ensure_ascii=False
#         json_result = json.dumps(menu_items, ensure_ascii=False, default=custom_json_serializer)
        
#         response = app.response_class(
#             response=json_result,
#             status=200,
#             mimetype='application/json'
#         )
#         response.headers['Content-Type'] = 'application/json; charset=utf-8'
#         return response
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import json
from decimal import Decimal
from datetime import datetime, date
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    conn.set_client_encoding('UTF8')
    return conn

def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

def get_restaurant(data):
    print(data)
    campus = data.get('campus')
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        if campus:
            print("有輸入")
            # Query to fetch restaurant_ids based on campus
            query = """
                SELECT r.restaurant_id, r.type AS restaurant_type, r.name AS restaurant_name, r.image_url
                FROM restaurants r
                JOIN restaurants_stands rs ON r.restaurant_id = rs.restaurant_id
                WHERE rs.campus = %s
                ORDER BY r.restaurant_id;
            """
            cursor.execute(query, (campus,))
        else:
            print("沒輸入")
            # Query to fetch all restaurants
            query = """
                SELECT restaurant_id, type AS restaurant_type, name AS restaurant_name, image_url
                FROM restaurants
                ORDER BY restaurant_id;
            """
            cursor.execute(query)

        restaurants = cursor.fetchall()

        cursor.close()
        conn.close()

        json_result = json.dumps(restaurants, ensure_ascii=False, default=custom_json_serializer)

        response = app.response_class(
            response=json_result,
            status=200,
            mimetype='application/json'
        )
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500