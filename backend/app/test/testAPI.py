import requests


base_url = "http://127.0.0.1:5000"

# home url
response = requests.get(f"{base_url}/")
print("Home endpoint response:", response.text)

# order history url
post_data = {
  "start_date": "2024-05-01",
  "end_date": "2024-05-30",
  "customer_id": "user01"
}
response = requests.post(f"{base_url}/api/orderHistory", json=post_data)
print("POST /api/data response:", response.json())

# get rating
post_data = {
  "item_id" : "item001"
}
response = requests.post(f"{base_url}/api/getRating", json=post_data)
print("POST /api/data response:", response.json())

# update rating
post_data = {
  "user_id": "user01", "item_id": 'item001', "rating": "1.7"
}
# response = requests.post(f"{base_url}/api/updateRating", json=post_data)
# print("POST /api/data response:", response.json())

# payment notification
post_data = {
  "user_id": ['user01', 'user02', 'user03']
}
# response = requests.post(f"{base_url}/api/paymentNotification", json=post_data)
# print("POST /api/data response:", response.json())

# payment
post_data = {
  "order_id": 1, 
  "customer_id" : "user03", 
  "payment_method" : "credit card"
}
response = requests.post(f"{base_url}/api/payment", json=post_data)
print("POST /api/data response:", response.json())