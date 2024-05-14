from flask import Flask, jsonify, request

from services import order_history, get_rating

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, I am alive!'

# get order history
@app.route('/api/orderHistory', methods=['GET'])
def get_order_history():
    data = order_history.get_order_history(request.get_json())
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
