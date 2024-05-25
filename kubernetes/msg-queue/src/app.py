from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime
from lib.iac_config_helper import IACConfigHelper
import pytz

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
