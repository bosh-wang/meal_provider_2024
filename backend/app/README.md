# mealprovider2024
mealprovider2024
### Run Flask on Docker
1. build the Flask image
```shell
docker build backend_image .
```
2. run docker using port-forwarding
```shell
docker -p 5000:5000 backend_image --name backend_api
```
### Run Flask on localhost
### Set up Python environment
```shell
cd backend
pip install -r requirements.txt
```

### Connect to K8s PostgreSQL
```shell
kubectl port-forward pods/citus-coordinator-0 5432:5432
```

### Run Flask server
```shell
cd backend/app
python main.py
```
#### api server will run on `localhost:5000`



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
pip install -r requirements.txt
cd app/
python main.py

```

# 取得資料庫資料 get_information.py
python get_information.py
curl -X GET http://localhost:5000/api/get_information
# 點餐 order_service.py
```
curl -X POST -H "Content-Type: application/json" -d @services/orders.json http://localhost:5000/api/create_order

```
更改訂單狀態
```
curl -X POST -H "Content-Type: application/json" -d @services/status_change.json http://localhost:5000/api/change_order_status
```
取得訂單狀態
```
curl -X GET "http://localhost:5000/api/get_order?order_id=3"
```

# 取得菜單 get_menu_service.py
```
curl -X GET http://localhost:5000/api/menu

curl -X POST -H "Content-Type: application/json" -d @services/menu.json http://localhost:5000/api/menu
```

# 登入 signin_service.py
```
curl -X POST -H "Content-Type: application/json" -d @services/signin.json http://localhost:5000/api/signin
```

# 更改菜單 adjust_menu_service.py
```
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