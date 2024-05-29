import os
import json
from google.cloud import pubsub_v1
import psycopg2
from datetime import datetime
from lib.iac_config_helper import IACConfigHelper
from lib.pg_helper import PGConnect

# Set up environment variables for Google Cloud Pub/Sub and PostgreSQL
config_path = "config/credential.yaml"
config = IACConfigHelper.get_conn_info(config_path)
pubsub_config = config["gcp"]["pubsub"]
project_id = config["gcp"]["pubsub"]["project_id"]
subscription_id = config["gcp"]["pubsub"]["subscription_id"]
credentials_path = config["gcp"]["credentials"]
subscriber = pubsub_v1.SubscriberClient.from_service_account_json(credentials_path)
print(subscriber)
subscription_path = subscriber.subscription_path(project_id, subscription_id)


def process_status_update(message):
    order_data = json.loads(message.data)
    conn = psycopg2.connect(
        dbname=config["database"]["postgres"]["dbname"],
        user=config["database"]["postgres"]["user"],
        password=config["database"]["postgres"]["password"],
        host=config["database"]["postgres"]["host"],
        port=config["database"]["postgres"]["port"],
    )
    cursor = conn.cursor()

    try:
        if order_data["status"] == "PENDING":
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

        elif order_data["status"] in ["CONFIRMED", "PREPARED", "COMPLETED", "CANCELED"]:
            status_field = {
                "CONFIRMED": "confirmed_date",
                "PREPARED": "prepared_date",
                "COMPLETED": "completed_date",
                "CANCELED": "canceled_date",
            }[order_data["status"]]
            cursor.execute(
                f"""
                UPDATE orders SET order_status = %s, {status_field} = %s
                WHERE order_id = %s
            """,
                (order_data["status"], datetime.now(), order_data["order_id"]),
            )

        conn.commit()
        message.ack()
    except Exception as e:
        conn.rollback()
        print(f"Failed to process order: {e}")
    finally:
        cursor.close()
        conn.close()


streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=process_status_update
)
print(f"Listening for messages on {subscription_path}")

with subscriber:
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
