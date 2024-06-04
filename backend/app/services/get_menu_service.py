from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
import json
from decimal import Decimal
from datetime import datetime, date
import os
import redis
from datetime import timedelta
import time

app = Flask(__name__)

# 连接到 Redis，加入密码认证
pool = redis.ConnectionPool(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    db=0,
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=pool)


# Database connection configuration
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )
    conn.set_client_encoding("UTF8")
    return conn


def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


def get_menu(data):
    r_id = data.get("restaurant_id")
    role = data.get("role")

    try:
        cache_key = f"menu:{r_id,role}"
        cache_expiry = timedelta(hours=1)

        start_time = time.time()  # Start timing for Redis

        # Check if the data is in Redis cache
        cached_menu = redis_client.get(cache_key)

        if cached_menu:
            redis_time = time.time() - start_time  # Calculate Redis time
            print(f"Cache hit, Time taken with Redis: {redis_time:.6f} seconds")
            return app.response_class(
                response=cached_menu, status=200, mimetype="application/json"
            )
        start_time = time.time()  # Start timing for DB query
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        if role == "employee":
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
                    m.restaurant_id = %s AND m.availability = True
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
        elif role == "restaurant_staff" or role == "HR":
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
        else:
            return jsonify({"error": "Invalid role"}), 400

        menu_items = cursor.fetchall()

        cursor.close()
        conn.close()
        db_time = time.time() - start_time  # Calculate DB query time
        print(f"Time taken with DB: {db_time:.6f} seconds")

        json_result = json.dumps(
            menu_items, ensure_ascii=False, default=custom_json_serializer
        )
        # Store the result in Redis cache
        redis_client.setex(cache_key, cache_expiry, json_result)
        response = app.response_class(
            response=json_result, status=200, mimetype="application/json"
        )
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_item(data):
    print("來這裡囉")
    item_id = data.get("item_id")

    if not item_id:
        return jsonify({"error": "Missing item_id"}), 400

    try:
        cache_key = f"item:{item_id}"
        cache_expiry = timedelta(hours=1)

        start_time = time.time()

        # Check if the data is in Redis cache
        cached_item = redis_client.get(cache_key)

        if cached_item:
            redis_time = time.time() - start_time
            print(f"Cache hit, Time taken with Redis: {redis_time:.6f} seconds")
            return app.response_class(
                response=cached_item, status=200, mimetype="application/json"
            )

        start_time = time.time()
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
                m.item_id = %s
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
                m.image_url;
        """
        cursor.execute(query, (item_id,))

        item = cursor.fetchone()

        cursor.close()
        conn.close()
        db_time = time.time() - start_time
        print(f"Time taken with DB: {db_time:.6f} seconds")

        if item is None:
            return jsonify({"error": "Item not found"}), 404

        json_result = json.dumps(
            item, ensure_ascii=False, default=custom_json_serializer
        )
        # Store the result in Redis cache
        redis_client.setex(cache_key, cache_expiry, json_result)
        response = app.response_class(
            response=json_result, status=200, mimetype="application/json"
        )
        print(response)
        print(json_result)
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
