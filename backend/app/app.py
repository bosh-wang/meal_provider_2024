from flask import Flask, jsonify, request

# Importing services
from services import (
    signin_service,
    order_service,
    get_menu_service,
    adjust_menu_service,
)

app = Flask(__name__)


@app.route("/backend/")
def index():
    return "Hello, I am alive!"


# 登入 合體成功
@app.route("/api/signin", methods=["POST"])
def signin():
    data = request.json
    return signin_service.signin(data)


# 下訂單 合體完成
# Create order
@app.route("/api/create_order", methods=["POST"])
def create_order():
    data = request.json
    return order_service.create_order(data)


# Change order status
@app.route("/api/change_order_status", methods=["POST"])
def change_order_status():
    data = request.json
    return order_service.change_order_status(data)


# Get order
@app.route("/api/get_order", methods=["GET"])
def get_order():
    order_id = request.args.get("order_id")
    return order_service.get_order(order_id)


# Get menu 合體成功
@app.route("/api/menu", methods=["GET"])
def get_menu():
    # data = get_menu_service.get_menu()
    # return jsonify(data)
    return get_menu_service.get_menu()


# Adjust menu 刪除還有點問題
@app.route("/api/change_menu_item", methods=["POST"])
def adjust_menu():
    # data = adjust_menu_service.adjust_menu()
    # return jsonify(data)
    return adjust_menu_service.change_menu_item()


# Payment notification
@app.route("/api/paymentNotification", methods=["GET"])
def payment_notify():
    data = payment_service.payment_notification_service()
    return jsonify(data)


@app.route("/api/payment", methods=["POST"])
def payment():
    data = payment_service.payment(request.get_json())
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
