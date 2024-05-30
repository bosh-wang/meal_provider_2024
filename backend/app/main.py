from flask import Flask, jsonify, request

from services import rating_service, order_history_service, payment_service, signin_service, order_service, get_menu_service, adjust_menu_service, get_restaurants_service,cart_service

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, I am alive!'

# get order history for employee
@app.route('/api/orderHistoryEmployee', methods=['POST'])
def get_order_history_employee():
    data = order_history_service.get_order_history_service_for_employee(request.get_json())
    return jsonify(data)

# get order history for hr
@app.route('/api/orderHistoryHR', methods=['POST'])
def get_order_history_hr():
    data = order_history_service.get_order_history_service_for_hr(request.get_json())
    return jsonify(data)

# get order history for restaurant
def get_order_history_restaurant():
    data = order_history_service.get_order_history_service_for_restaurant(request.get_json())
    return jsonify(data)

# get rating
@app.route('/api/getRating', methods=['POST'])
def get_rating():
    data = rating_service.get_rating_service(request.get_json())
    return jsonify(data)

# update rating
@app.route('/api/updateRating', methods=['POST'])
def update_rating():
    data = rating_service.update_rating_service(request.get_json())
    return jsonify(data)

# payment notification
@app.route('/api/paymentNotification', methods=['POST'])
def payment_notiy():
    data = payment_service.payment_notification_service(request.get_json())#
    return jsonify(data)

@app.route('/api/payment', methods=['POST'])
def payment():
    data = payment_service.payment(request.get_json())
    return jsonify(data)

# test
@app.route('/api/test', methods=['get'])
def test():
    data = order_history_service.test()
    return jsonify(data)

# 登入
@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.json
    return signin_service.signin(data)

# Get menu
@app.route('/api/menu', methods=['POST'])
def get_menu():
    data = request.json
    return get_menu_service.get_menu(data)

# 取得餐廳
@app.route('/api/restaurants', methods=['POST'])
def get_restaurant():
    data = request.json
    return get_restaurants_service.get_restaurant(data)

# Adjust menu 刪除還有點問題
@app.route('/api/change_menu_item', methods=['POST'])
def adjust_menu():
    return adjust_menu_service.change_menu_item()



## 訂單部分
# Create order
@app.route('/api/create_order', methods=['POST'])
def create_order():
    data = request.json
    return order_service.create_order(data)

# Change order status
@app.route('/api/change_order_status', methods=['POST'])
def change_order_status():
    data = request.json
    return order_service.change_order_status(data)

# Get order
@app.route('/api/get_order', methods=['POST'])
def get_order():
    data = request.json
    return order_service.get_order(data)

## 購物車
@app.route('/api/update_cart', methods=['POST'])
def update_cart():
    data = request.json
    return cart_service.handle_cart(data)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)