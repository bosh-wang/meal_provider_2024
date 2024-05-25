# mealprovider2024
mealprovider2024

```
mkdir ~/.kube
code ~/.kube/config
```
貼上資料
```
kubectl port-forward pods/citus-coordinator-0 5432:5432
```
開另一個終端機
```
cd backend/
pip install flask
pip install psycopg2
```

# 點餐
```
curl -X POST -H "Content-Type: application/json" -d @orders.json http://localhost:5000/create_order
```
更改狀態
```
curl -X POST -H "Content-Type: application/json" -d @status_change.json http://localhost:5000/change_order_status
```
取得訂單狀態
```
curl -X GET "http://localhost:5000/get_order?order_id=2"
```
# 取得菜單
```
python app.py
curl -X GET http://localhost:5000/menu
```
# 登入
```
python sign.py
```
# 更改菜單
```
python menu_1change.py 

curl -X POST -H "Content-Type: application/json" -d @menu_add.json http://localhost:5000/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @menu_delete.json http://localhost:5000/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @menu_adjust.json http://localhost:5000/change_menu_item
```
或是
```
curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADD", "restaurant_id": "restaurant001", "category": "Main Course", "item_name": "Spaghetti", "description": "Classic spaghetti with tomato sauce", "price": 10.99, "availability": true, "image_url": "https://example.com/spaghetti.jpg"}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADJUST", "item_name": "Spaghetti", "price": 12.99}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "DELETE", "item_name": "Spaghetti"}' http://localhost:5000/change_menu_item
```