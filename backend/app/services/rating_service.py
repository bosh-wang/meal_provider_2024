from datetime import datetime
import mysql.connector

def get_rating_service():#data

    # conn = mysql.connector.connect(
    # host='localhost',           
    # user='user',               
    # password='@MySQLPassword', 
    # )
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
    #     return ({"item_id": item_id, "rating": rating})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return(
        {
        "item_id": "A4564F4",
        "rating": 4,
        "review_date": "2024-03-15"
        })


def update_rating_service():#data
    conn = mysql.connector.connect(
    host='localhost',           
    user='user',               
    password='@MySQLPassword', 
    )
    # cursor = conn.cursor()

    # try:
    #     item_id = data['item_id']
    #     rating = data['rating']

    #     cursor.execute("INSERT INTO VALUES")

    #     cursor.close()
    #     return ({"message" : "successfully inserted rating"})
    # except Exception as e:
    #     return ({"error": str(e)}), 500
    return ({"message" : "successfully inserted rating"})