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
    "restaurant_id": "restaurant003"
}
response = requests.post(f"{base_url}/api/menu", json=post_data)
print("POST /api/data response:", response.json())


#adjust menu
post_data = {
    "change_status": "ADD",
    "restaurant_id": "restaurant003",
    "category": "主食",
    "item_name": "超級爆炸天啊好吃牛肉丸",
    "description": "吃四年都吃不膩",
    "price": 160,
    "availability": 'False', #測試用
    "image_url": "https://images.app.goo.gl/q4aVdPB83r7kHM1d7"
}
response = requests.post(f"{base_url}/api/adjust_menu", json=post_data)
print("POST /api/data response:", response.json())


# order


#change order status

#check order status





## 購物車部分

# 加入購物車

# 查看購物車

# 更新購物車

# 刪除整個購物車

