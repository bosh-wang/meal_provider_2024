from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os


def get_rating_service():  # data
    # host = os.getenv("DB_HOST")
    # dbname = os.getenv("DB_NAME")
    # user = os.getenv("DB_USER")
    # password = os.getenv("DB_PASSWORD")
    # sslmode = "require"
    # conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    # conn = psycopg2.connect(conn_string)
    # print("Connection established")
    # cursor = conn.cursor()

    # try:
    #     item_id = data['item_id']

    #     cursor.execute("SELECT  FROM  WHERE")
    #     ratings = cursor.fetchall()

    #     rating = None
    #     for r in ratings:
    #         rating += r

    #     rating /= len(ratings)

    #     cursor.close()
    # conn.close()
    #     return ({"item_id": item_id, "rating": rating})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return {"item_id": "A4564F4", "rating": 4, "review_date": "2024-03-15"}


def update_rating_service():  # data
    # host = os.getenv("DB_HOST")
    # dbname = os.getenv("DB_NAME")
    # user = os.getenv("DB_USER")
    # password = os.getenv("DB_PASSWORD")
    # sslmode = "require"
    # conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    # conn = psycopg2.connect(conn_string)
    # print("Connection established")
    # cursor = conn.cursor()

    # try:
    #     item_id = data['item_id']
    #     rating = data['rating']

    #     cursor.execute("INSERT INTO VALUES")

    #     cursor.close()
    #     conn.close()
    #     return ({"message" : "successfully inserted rating"})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return {"message": "successfully inserted rating"}
