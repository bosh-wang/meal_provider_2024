## mealprovider2024
=======
mealprovider2024

```
mkdir ~/.kube
code ~/.kube/config
```
貼上資料
```
kubectl port-forward pods/citus-coordinator-0 5432:5432
kubectl port-forward pods/redis-deployment-6fd8c6db4d-jcbsr 6379:6379
```
開另一個終端機
```
cd backend/
pip install requirements.txt
cd app/
```
# 取得資料庫資料 get_information.py
python get_information.py

# 點餐 order_service.py
```
curl -X POST -H "Content-Type: application/json" -d @services/orders.json http://localhost:5000/api/create_order
<!-- curl -X POST -H "Content-Type: application/json" -d @orders.json http://localhost:5000/create_order -->
```
更改狀態
```
curl -X POST -H "Content-Type: application/json" -d @services/status_change.json http://localhost:5000/api/change_order_status
<!-- curl -X POST -H "Content-Type: application/json" -d @status_change.json http://localhost:5000/change_order_status -->
```
取得訂單狀態
```
curl -X GET "http://localhost:5000/api/get_order?order_id=3"
<!-- curl -X GET "http://localhost:5000/get_order?order_id=2" -->
```
# 取得菜單 get_menu_service.py
```
curl -X GET http://localhost:5000/api/menu
<!-- python get_menu_service.py
curl -X GET http://localhost:5000/menu -->
```
# 登入 signin_service.py
```
<!-- python signin_service.py -->
curl -X POST -H "Content-Type: application/json" -d @services/signin.json http://localhost:5000/api/signin
```
# 更改菜單 adjust_menu_service.py
```
python adjust_menu_service.py

curl -X POST -H "Content-Type: application/json" -d @services/menu_add.json http://localhost:5000/api/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @services/menu_delete.json http://localhost:5000/api/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @services/menu_adjust.json http://localhost:5000/api/change_menu_item
```
或是
```
curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADD", "restaurant_id": "restaurant001", "category": "Main Course", "item_name": "Spaghetti", "description": "Classic spaghetti with tomato sauce", "price": 10.99, "availability": true, "image_url": "https://example.com/spaghetti.jpg"}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADJUST", "item_name": "Spaghetti", "price": 12.99}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "DELETE", "item_name": "Spaghetti"}' http://localhost:5000/change_menu_item
```

### System
