import requests


base_url = "http://127.0.0.1:5000"  # "http://35.224.128.24"

# home url
response = requests.get(f"{base_url}/")
print("Home endpoint response:", response.text)

print("=" * 10)

# order history employee url
post_data = {
    "start_date": "2024-05-01",
    "end_date": "2024-05-30",
    "customer_id": "user01",
}
response = requests.post(f"{base_url}/api/orderHistoryEmployee", json=post_data)
print("POST /api/data response:", response.json())
print("=" * 10)

# order history restaurant url
post_data = {
    "start_date": "2024-05-01",
    "end_date": "2024-05-30",
    "restaurant_id": "restaurant003",
}
response = requests.post(f"{base_url}/api/orderHistoryRestaurant", json=post_data)
print("POST /api/data response:", response.json())
print("=" * 10)

# order history hr url
post_data = {
    "start_date": "2024-05-01",
    "end_date": "2024-05-30",
}
response = requests.post(f"{base_url}/api/orderHistoryHR", json=post_data)
print("POST /api/data response:", response.json())
print("=" * 10)

# get rating
post_data = {"item_id": "item001"}
response = requests.post(f"{base_url}/api/getRating", json=post_data)
print("POST /api/data response:", response.json())
print("=" * 10)

# update rating
post_data = {"user_id": "user01", "item_id": "item001", "rating": "1.7"}
# response = requests.post(f"{base_url}/api/updateRating", json=post_data)
# print("POST /api/data response:", response.json())
# print('='*10)

# payment notification
post_data = {"user_id": ["user01", "user02", "user03"]}
# response = requests.post(f"{base_url}/api/paymentNotification", json=post_data)
# print("POST /api/data response:", response.json())
# print('='*10)

# payment
post_data = {"order_id": 1, "customer_id": "user03", "payment_method": "credit card"}
# response = requests.post(f"{base_url}/api/payment", json=post_data)
# print("POST /api/data response:", response.json())
