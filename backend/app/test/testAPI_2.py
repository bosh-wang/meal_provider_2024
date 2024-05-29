import requests


base_url = "http://127.0.0.1:5000"

# home url
response = requests.get(f"{base_url}/")
print("Home endpoint response:", response.text)

# sign in url
post_data = {
    "role": "restaurant_staff",
    "email": "ranbirkapoor@tsmc.com",
    "password_hash": "0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e"
}
response = requests.post(f"{base_url}/api/signin", json=post_data)
print("POST /api/data response:", response.json())

#get restaurant 
response = requests.get(f"{base_url}/api/restaurants")
print("GET /api/data response:", response.json())

#get menu
post_data = {
    "restaurant_id": "restaurant040"
}
response = requests.post(f"{base_url}/api/menu", json=post_data)
print("POST /api/data response:", response.json())


# order
# post_data = 


#change order status

#check order status

#adjust menu


