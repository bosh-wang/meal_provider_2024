from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

# from config import load_config
import os

app = Flask(__name__)


# Database connection configuration
def get_db_connection():
    # config = load_config()
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )
    conn.set_client_encoding("UTF8")
    return conn


@app.route("/api/get_information", methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        select_query = "SELECT * FROM restaurants_stands;"
        # 取得各個table的資料:menus_items meals_ratings users orders_items items
        cur.execute(select_query)
        users = cur.fetchall()

        cur.close()
        conn.close()

        response = jsonify(users)
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
