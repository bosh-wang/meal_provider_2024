from flask import jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from config import load_config
import os


# 取得config內的資訊
def get_db_connection():
    # config = load_config()
    return psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
        # database=config['GCP']['database'],
        # host=config['GCP']['host'],
        # user=config['GCP']['user'],
        # password=config['GCP']['password'],
        # port=config['GCP']['port']
    )

def sign_in(r, cID, passw):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        select_query = """
        SELECT user_id, username, password_hash, role, email
        FROM users
        WHERE email = %s AND role = %s AND password_hash = %s;
        """

        cur.execute(select_query, (cID, r, passw))
        result = cur.fetchone()

        if result:
            data = {
                "message": "Login Successful"
            }
            response = jsonify(data)
            response.status_code = 200
        else:
            data = {
                "message": "Login failed"
            }
            response = jsonify(data)
            response.status_code = 401
        cur.close()
        conn.close()
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def signin(data):
    r = data.get('role')
    cID = data.get('email')
    passw = data.get('password_hash')

    if not (r and cID and passw):
        return jsonify({"error": "少了一些參數"}), 400

    return sign_in(r, cID, passw)
