from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime
from lib.iac_config_helper import IACConfigHelper
import pytz
from psycopg2.extras import RealDictCursor
import json
from datetime import datetime, date
from decimal import Decimal
import redis
import os
from datetime import timedelta
import time

app = Flask(__name__)
config_path = "config/credential.yaml"
conn_config = IACConfigHelper.get_conn_info(config_path)

# Set up environment variables for PostgreSQL
config_path = "config/credential.yaml"
conn_config = IACConfigHelper.get_conn_info(config_path)
db_config = conn_config["database"]["postgres"]
tz = pytz.timezone("Asia/Taipei")


def get_db_connection():
    conn = psycopg2.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
    )
    return conn


@app.route("/order", methods=["POST"])
def create_order():
    try:
        order_data = request.json
        if not order_data:
            app.logger.error("Invalid input: %s", request.data)
            return jsonify({"error": "Invalid input"}), 400

        app.logger.info("Order received: %s", order_data)
        order_data["status"] = "PENDING"
        # Get current time in UTC+8
        order_data["order_date"] = datetime.now(tz)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO orders (user_id, restaurant_id, total_price, order_date, order_status)
            VALUES (%s, %s, %s, %s, %s) RETURNING order_id
        """,
            (
                order_data["user_id"],
                order_data["restaurant_id"],
                order_data["total_price"],
                order_data["order_date"],
                order_data["status"],
            ),
        )
        order_id = cursor.fetchone()[0]

        for detail in order_data["order_details"]:
            cursor.execute(
                """
                INSERT INTO orders_items (order_id, item_id, quantity, price)
                VALUES (%s, %s, %s, %s)
            """,
                (order_id, detail["item_id"], detail["quantity"], detail["price"]),
            )

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Order created", "order": order_data}), 201
    except Exception as e:
        app.logger.error("Error creating order: %s", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/order/status", methods=["POST"])
def update_order_status():
    try:
        status_update = request.json
        if not status_update:
            app.logger.error("Invalid input: %s", request.data)
            return jsonify({"error": "Invalid input"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        status_field = {
            "CONFIRMED": "confirmed_date",
            "PREPARED": "prepared_date",
            "COMPLETED": "completed_date",
            "CANCELED": "canceled_date",
        }.get(status_update["status"])

        if status_field:
            cursor.execute(
                f"""
                UPDATE orders SET order_status = %s, {status_field} = %s
                WHERE order_id = %s
            """,
                (status_update["status"], datetime.now(tz), status_update["order_id"]),
            )
        else:
            cursor.execute(
                """
                UPDATE orders SET order_status = %s
                WHERE order_id = %s
            """,
                (status_update["status"], status_update["order_id"]),
            )

        conn.commit()
        cursor.close()
        conn.close()
        return (
            jsonify({"message": "Order status updated", "status": status_update}),
            200,
        )
    except Exception as e:
        app.logger.error("Error updating order status: %s", str(e))
        return jsonify({"error": str(e)}), 500


def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


# 连接到 Redis，加入密码认证
pool = redis.ConnectionPool(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    db=0,
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=pool)


@app.route("/get_menu", methods=["POST"])
def get_menu():
    data = request.get_json()
    r_id = data.get("restaurant_id")

    try:
        cache_key = f"menu:{r_id}"
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
