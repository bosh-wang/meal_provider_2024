from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

@app.route('/')
def index():
    return 'Hello, I am alive!'

# Route to get all data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
