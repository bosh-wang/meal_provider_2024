import requests


base_url = "http://127.0.0.1:5000"

# home url
response = requests.get(f"{base_url}/")
print("Home endpoint response:", response.text)

# # # sign in
# post_data = {"password": "~j@;_R,.qD=|", "role": "HR", "email": "hughjackman@tsmc.com"}
# response = requests.post(f"{base_url}/api/signin", json=post_data)
# print("POST /api/data response:", response.json())


# "role": "restaurant_staff",
# "email": "ranbirkapoor@tsmc.com",
# "password": "*fqyav|){Nc0"


# "password": ":]!,-[^N86Lj",
# "role": "employee",
# "email": "jakegyllenhaal@tsmc.com"


# # get restaurant
# post_data = {"campus": "竹科竹科園區"}

# response = requests.post(f"{base_url}/api/restaurants", json=post_data)
# print("POST /api/data response:", response.json())
# post_data = {
# }
# response = requests.post(f"{base_url}/api/restaurants", json=post_data)
# print("POST /api/data response:", response.json())


# # get menu
## 餐廳管理員
# post_data = {
#     "role": "restaurant_staff",
#     "restaurant_id": "restaurant003"
# }
## 員工
post_data = {"role": "HR", "restaurant_id": "restaurant003"}
response = requests.post(f"{base_url}/api/menu", json=post_data)
print(response)
print("POST /api/data response:", response.json())

# api/menu_item
post_data = {"item_id": "item809"}
response = requests.post(f"{base_url}/api/menu_item", json=post_data)
print(response)
print("POST /api/data response:", response.json())


# post_data = {"role": "restaurant_staff", "restaurant_id": "restaurant007"}
# response = requests.post(f"{base_url}/api/menu", json=post_data)
# print("POST /api/data response:", response.json())
# # adjust menu-add
# post_data = {
#     "change_status": "ADD",
#     "restaurant_id": "restaurant003",
#     "category": "主食",
#     "item_name": "超級爆炸天啊好吃牛肉丸",
#     "description": "吃四年都吃不膩",
#     "price": 160,
#     "availability": False, #測試用
#     "image_url": "https://images.app.goo.gl/q4aVdPB83r7kHM1d7"
# }

# # adjust menu-price change
# post_data = {
#     "change_status": "ADJUST",
#     "item_id": "item809",
#     "price": 190
# }

# # adjust menu-availability false
# post_data ={
#     "change_status": "DELETE",
#     "item_id": "item809",
#     "availability": False
# }
# response = requests.post(f"{base_url}/api/change_menu_item", json=post_data)
# print("POST /api/data response:", response.json())


# order
# post_data ={
#   "user_id": "user01",
#   "restaurant_id": "restaurant040",
#   "items": [
#       {"item_id": "item789", "quantity": 2},
#       {"item_id": "item790", "quantity": 1}
#   ]
# }
# response = requests.post(f"{base_url}/api/create_order", json=post_data)
# print("POST /api/data response:", response.json())

# # change order status 好像要先改成去資料庫抓
# post_data ={
#     "order_id": 14,
#     "order_status_before": "PENDING",
#     "order_status_after": "CONFIRMED"
# }
# response = requests.post(f"{base_url}/api/change_order_status", json=post_data)
# print("POST /api/data response:", response.json())


# # check order status
# post_data ={
#     "order_id": 14
# }
# response = requests.post(f"{base_url}/api/get_order", json=post_data)
# print("POST /api/data response:", response.json())


## 購物車部分
# # 更新購物車
# post_data = {
#     "cart_status": "update",
#     "user_id": "user03",
#     "item_id": "item023",
#     "quantity": 2,
# }
# response = requests.post(f"{base_url}/api/update_cart", json=post_data)
# print("POST /api/data response:", response.json())


# # 查看購物車
# post_data = {"cart_status": "check", "user_id": "user03"}

# #送出訂單
# post_data ={
#    "cart_status": "submit",
#    "user_id": "user03"
# }
# response = requests.post(f"{base_url}/api/update_cart", json=post_data)
# print("POST /api/data response:", response.json())
