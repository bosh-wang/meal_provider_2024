from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import os

# Call create_order from order_service
from . import order_service


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


def update_cart_item(data):
    user_id = data["user_id"]
    item_id = data["item_id"]
    quantity = data["quantity"]
    current_time = datetime.utcnow().isoformat()

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Check the restaurant of the item being added or updated
        restaurant_check_query = """
            SELECT r.restaurant_id
            FROM menus_items mi
            JOIN restaurants r ON mi.restaurant_id = r.restaurant_id
            WHERE mi.item_id = %s
        """
        cursor.execute(restaurant_check_query, (item_id,))
        item_restaurant = cursor.fetchone()

        if not item_restaurant:
            return jsonify({"error": "Item not found"}), 404

        item_restaurant_id = item_restaurant["restaurant_id"]

        # Check if there are existing items in the cart from a different restaurant
        existing_restaurant_query = """
            SELECT DISTINCT r.restaurant_id
            FROM shopping_cart sc
            JOIN menus_items mi ON sc.item_id = mi.item_id
            JOIN restaurants r ON mi.restaurant_id = r.restaurant_id
            WHERE sc.user_id = %s AND sc.status = 'ACTIVE'
        """
        cursor.execute(existing_restaurant_query, (user_id,))
        existing_restaurants = cursor.fetchall()

        if existing_restaurants and any(
            r["restaurant_id"] != item_restaurant_id for r in existing_restaurants
        ):
            return (
                jsonify({"error": "Cannot add items from different restaurants"}),
                400,
            )

        if quantity == 0:
            # Remove item from cart
            delete_query = """
                DELETE FROM shopping_cart 
                WHERE user_id = %s AND item_id = %s AND status = 'ACTIVE'
                RETURNING cart_id;
            """
            cursor.execute(delete_query, (user_id, item_id))
            removed_cart = cursor.fetchone()
            conn.commit()
            cursor.close()
            conn.close()
            if removed_cart:
                return (
                    jsonify(
                        {
                            "message": "Item removed from cart",
                            "cart_id": removed_cart["cart_id"],
                        }
                    ),
                    200,
                )
            else:
                return jsonify({"error": "Item not found in cart"}), 404
        else:
            # Check if item already exists in cart
            check_query = """
                SELECT cart_id FROM shopping_cart 
                WHERE user_id = %s AND item_id = %s AND status = 'ACTIVE'
            """
            cursor.execute(check_query, (user_id, item_id))
            existing_cart = cursor.fetchone()

            if existing_cart:
                # Update existing item quantity
                update_query = """
                    UPDATE shopping_cart
                    SET quantity = %s, updated_at = %s
                    WHERE cart_id = %s
                    RETURNING cart_id;
                """
                cursor.execute(
                    update_query, (quantity, current_time, existing_cart["cart_id"])
                )
                updated_cart = cursor.fetchone()
                conn.commit()
                cursor.close()
                conn.close()
                return (
                    jsonify(
                        {
                            "message": "Cart item updated",
                            "cart_id": updated_cart["cart_id"],
                        }
                    ),
                    200,
                )
            else:
                # Add new item to cart
                get_max_cart_id_query = "SELECT COALESCE(MAX(cart_id), 0) + 1 AS new_cart_id FROM shopping_cart"
                cursor.execute(get_max_cart_id_query)
                new_cart_id = cursor.fetchone()["new_cart_id"]

                insert_query = """
                    INSERT INTO shopping_cart (cart_id, user_id, item_id, quantity, status, added_at, updated_at)
                    VALUES (%s, %s, %s, %s, 'ACTIVE', %s, %s)
                    RETURNING cart_id;
                """
                cursor.execute(
                    insert_query,
                    (
                        new_cart_id,
                        user_id,
                        item_id,
                        quantity,
                        current_time,
                        current_time,
                    ),
                )
                new_cart = cursor.fetchone()
                conn.commit()
                cursor.close()
                conn.close()
                return (
                    jsonify(
                        {"message": "Cart item added", "cart_id": new_cart["cart_id"]}
                    ),
                    201,
                )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_cart(data):
    user_id = data["user_id"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT sc.user_id, r.restaurant_id, r.name AS restaurant_name, m.item_id, sc.quantity
            FROM shopping_cart sc
            JOIN menus_items m ON sc.item_id = m.item_id
            JOIN restaurants r ON m.restaurant_id = r.restaurant_id
            WHERE sc.user_id = %s AND sc.status = 'ACTIVE';
        """
        cursor.execute(query, (user_id,))
        cart_items = cursor.fetchall()

        cursor.close()
        conn.close()

        if not cart_items:
            return jsonify({"error": "No active items in cart"}), 404

        result = {
            "user_id": user_id,
            "restaurant_id": cart_items[0]["restaurant_id"],
            "restaurant_name": cart_items[0]["restaurant_name"],
            "items": [
                {"item_id": item["item_id"], "quantity": item["quantity"]}
                for item in cart_items
            ],
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def purchased(data):
    user_id = data["user_id"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Fetch all ACTIVE cart items for the user
        fetch_active_items_query = """
            SELECT sc.item_id, sc.quantity, r.restaurant_id
            FROM shopping_cart sc
            JOIN menus_items mi ON sc.item_id = mi.item_id
            JOIN restaurants r ON mi.restaurant_id = r.restaurant_id
            WHERE sc.user_id = %s AND sc.status = 'ACTIVE';
        """
        cursor.execute(fetch_active_items_query, (user_id,))
        active_items = cursor.fetchall()

        if not active_items:
            return jsonify({"error": "No active items in cart"}), 404

        # Check if all items are from the same restaurant
        restaurant_ids = {item["restaurant_id"] for item in active_items}
        if len(restaurant_ids) > 1:
            return (
                jsonify(
                    {"error": "All items in the cart must be from the same restaurant"}
                ),
                400,
            )

        # Construct the create_order payload
        restaurant_id = active_items[0]["restaurant_id"]
        items = [
            {"item_id": item["item_id"], "quantity": item["quantity"]}
            for item in active_items
        ]

        order_data = {
            "user_id": user_id,
            "restaurant_id": restaurant_id,
            "items": items,
        }

        order_service.create_order(order_data)

        # Update the cart items to set them as PURCHASED
        update_query = """
            UPDATE shopping_cart
            SET status = 'PURCHASED'
            WHERE user_id = %s AND status = 'ACTIVE';
        """
        cursor.execute(update_query, (user_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "成功送出訂單"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def handle_cart(data):
    # data = request.json
    print(data)
    cart_status = data.get("cart_status")
    print(cart_status)
    if cart_status == "update":
        return update_cart_item(data)
    elif cart_status == "check":
        return get_cart(data)
    elif cart_status == "submit":
        return purchased(data)
    else:
        return jsonify({"error": "Invalid cart_status"}), 400


# from flask import Flask, request, jsonify
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import json
# from datetime import datetime
# import os

# # Call create_order from order_service
# from . import order_service

# # app = Flask(__name__)


# def get_db_connection():
#     # config = load_config()
#     conn = psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         port=os.getenv("DB_PORT"),
#     )
#     conn.set_client_encoding("UTF8")
#     return conn


# def update_cart_item(data):
#     user_id = data["user_id"]
#     item_id = data["item_id"]
#     quantity = data["quantity"]
#     current_time = datetime.utcnow().isoformat()

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=RealDictCursor)

#         if quantity == 0:
#             # Remove item from cart
#             delete_query = """
#                 DELETE FROM shopping_cart
#                 WHERE user_id = %s AND item_id = %s AND status = 'ACTIVE'
#                 RETURNING cart_id;
#             """
#             cursor.execute(delete_query, (user_id, item_id))
#             removed_cart = cursor.fetchone()
#             conn.commit()
#             cursor.close()
#             conn.close()
#             if removed_cart:
#                 return (
#                     jsonify(
#                         {
#                             "message": "Item removed from cart",
#                             "cart_id": removed_cart["cart_id"],
#                         }
#                     ),
#                     200,
#                 )
#             else:
#                 return jsonify({"error": "Item not found in cart"}), 404
#         else:
#             # Check if item already exists in cart
#             check_query = """
#                 SELECT cart_id FROM shopping_cart
#                 WHERE user_id = %s AND item_id = %s AND status = 'ACTIVE'
#             """
#             cursor.execute(check_query, (user_id, item_id))
#             existing_cart = cursor.fetchone()

#             if existing_cart:
#                 # Update existing item quantity
#                 update_query = """
#                     UPDATE shopping_cart
#                     SET quantity = %s, updated_at = %s
#                     WHERE cart_id = %s
#                     RETURNING cart_id;
#                 """
#                 cursor.execute(
#                     update_query, (quantity, current_time, existing_cart["cart_id"])
#                 )
#                 updated_cart = cursor.fetchone()
#                 conn.commit()
#                 cursor.close()
#                 conn.close()
#                 return (
#                     jsonify(
#                         {
#                             "message": "Cart item updated",
#                             "cart_id": updated_cart["cart_id"],
#                         }
#                     ),
#                     200,
#                 )
#             else:
#                 # Add new item to cart
#                 get_max_cart_id_query = "SELECT COALESCE(MAX(cart_id), 0) + 1 AS new_cart_id FROM shopping_cart"
#                 cursor.execute(get_max_cart_id_query)
#                 new_cart_id = cursor.fetchone()["new_cart_id"]

#                 insert_query = """
#                     INSERT INTO shopping_cart (cart_id, user_id, item_id, quantity, status, added_at, updated_at)
#                     VALUES (%s, %s, %s, %s, 'ACTIVE', %s, %s)
#                     RETURNING cart_id;
#                 """
#                 cursor.execute(
#                     insert_query,
#                     (
#                         new_cart_id,
#                         user_id,
#                         item_id,
#                         quantity,
#                         current_time,
#                         current_time,
#                     ),
#                 )
#                 new_cart = cursor.fetchone()
#                 conn.commit()
#                 cursor.close()
#                 conn.close()
#                 return (
#                     jsonify(
#                         {"message": "Cart item added", "cart_id": new_cart["cart_id"]}
#                     ),
#                     201,
#                 )

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# def get_cart(data):
#     user_id = data["user_id"]

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=RealDictCursor)

#         query = """
#             SELECT sc.user_id, r.restaurant_id, r.name AS restaurant_name, m.item_id, sc.quantity
#             FROM shopping_cart sc
#             JOIN menus_items m ON sc.item_id = m.item_id
#             JOIN restaurants r ON m.restaurant_id = r.restaurant_id
#             WHERE sc.user_id = %s AND sc.status = 'ACTIVE';
#         """
#         cursor.execute(query, (user_id,))
#         cart_items = cursor.fetchall()

#         cursor.close()
#         conn.close()

#         if not cart_items:
#             return jsonify({"error": "No active items in cart"}), 404

#         result = {
#             "user_id": user_id,
#             "restaurant_id": cart_items[0]["restaurant_id"],
#             "restaurant_name": cart_items[0]["restaurant_name"],
#             "items": [
#                 {"item_id": item["item_id"], "quantity": item["quantity"]}
#                 for item in cart_items
#             ],
#         }

#         return jsonify(result), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# def purchased(data):
#     user_id = data["user_id"]

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=RealDictCursor)

#         # Fetch all ACTIVE cart items for the user
#         fetch_active_items_query = """
#             SELECT sc.item_id, sc.quantity, r.restaurant_id
#             FROM shopping_cart sc
#             JOIN menus_items mi ON sc.item_id = mi.item_id
#             JOIN restaurants r ON mi.restaurant_id = r.restaurant_id
#             WHERE sc.user_id = %s AND sc.status = 'ACTIVE';
#         """
#         cursor.execute(fetch_active_items_query, (user_id,))
#         active_items = cursor.fetchall()

#         if not active_items:
#             return jsonify({"error": "No active items in cart"}), 404

#         # Construct the create_order payload
#         restaurant_id = active_items[0]["restaurant_id"]
#         items = [
#             {"item_id": item["item_id"], "quantity": item["quantity"]}
#             for item in active_items
#         ]

#         order_data = {
#             "user_id": user_id,
#             "restaurant_id": restaurant_id,
#             "items": items,
#         }

#         order_service.create_order(order_data)

#         # Update the cart items to set them as PURCHASED
#         update_query = """
#             UPDATE shopping_cart
#             SET status = 'PURCHASED'
#             WHERE user_id = %s AND status = 'ACTIVE';
#         """
#         cursor.execute(update_query, (user_id,))
#         conn.commit()

#         cursor.close()
#         conn.close()

#         return jsonify({"message": "成功送出訂單"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# def handle_cart(data):
#     # data = request.json
#     print(data)
#     cart_status = data.get("cart_status")
#     print(cart_status)
#     if cart_status == "update":
#         return update_cart_item(data)
#     elif cart_status == "check":
#         return get_cart(data)
#     elif cart_status == "submit":
#         return purchased(data)
#     else:
#         return jsonify({"error": "Invalid cart_status"}), 400
