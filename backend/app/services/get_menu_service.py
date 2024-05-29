from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from config import load_config
import json
from decimal import Decimal
from datetime import datetime, date
import os

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    config = load_config()
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
    )
    conn.set_client_encoding('UTF8')
    return conn

def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")



def get_menu(data):
    r_id = data.get('restaurant_id')
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            SELECT 
                m.item_id,
                m.restaurant_id,
                r.type AS restaurant_type,
                r.name AS restaurant_name,
                m.category,
                m.item_name,
                m.description,
                m.price,
                m.availability,
                m.image_url,
                ROUND(AVG(rt.star_rating), 1) AS star_rating
            FROM 
                menus_items m
            LEFT JOIN 
                meals_ratings rt ON m.item_id = rt.item_id
            INNER JOIN
                restaurants r ON m.restaurant_id = r.restaurant_id
            WHERE 
                m.restaurant_id = %s
            GROUP BY 
                m.item_id,
                m.restaurant_id,
                r.type,
                r.name,
                m.category,
                m.item_name,
                m.description,
                m.price,
                m.availability,
                m.image_url
            ORDER BY 
                m.item_id;
        """
        
        cursor.execute(query, (r_id,))
        menu_items = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
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