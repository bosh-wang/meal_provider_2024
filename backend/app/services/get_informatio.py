from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from config import load_config

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    config = load_config()
    return psycopg2.connect(
        database=config['GCP']['database'],
        host=config['GCP']['host'],
        user=config['GCP']['user'],
        password=config['GCP']['password'],
        port=config['GCP']['port']
    )

@app.route('/api/get_information', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        select_query = "SELECT * FROM users;"
        # 取得各個table的資料:menus_items meals_ratings users orders_items items
        cur.execute(select_query)
        users = cur.fetchall()

        cur.close()
        conn.close()

        response = jsonify(users)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)