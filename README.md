## mealprovider2024
=======
mealprovider2024

## Backend Info
```bash
mkdir ~/.kube
code ~/.kube/config
```
貼上資料
```bash
kubectl port-forward pods/citus-coordinator-0 5432:5432
kubectl port-forward pods/redis-deployment-6fd8c6db4d-jcbsr 6379:6379
```
開另一個終端機
```bash
cd backend/
pip install requirements.txt
cd app/
```bash
## 取得資料庫資料 get_information.py
python get_information.py

## 點餐 order_service.py
```bash
curl -X POST -H "Content-Type: application/json" -d @services/orders.json http://localhost:5000/api/create_order
<!-- curl -X POST -H "Content-Type: application/json" -d @orders.json http://localhost:5000/create_order -->
```
更改狀態
```bash
curl -X POST -H "Content-Type: application/json" -d @services/status_change.json http://localhost:5000/api/change_order_status
<!-- curl -X POST -H "Content-Type: application/json" -d @status_change.json http://localhost:5000/change_order_status -->
```
取得訂單狀態
```bash
curl -X GET "http://localhost:5000/api/get_order?order_id=3"
<!-- curl -X GET "http://localhost:5000/get_order?order_id=2" -->
```
## 取得菜單 get_menu_service.py
```bash
curl -X GET http://localhost:5000/api/menu
<!-- python get_menu_service.py
curl -X GET http://localhost:5000/menu -->
```
## 登入 signin_service.py
```bash
<!-- python signin_service.py -->
curl -X POST -H "Content-Type: application/json" -d @services/signin.json http://localhost:5000/api/signin
```
## 更改菜單 adjust_menu_service.py
```bash
python adjust_menu_service.py

curl -X POST -H "Content-Type: application/json" -d @services/menu_add.json http://localhost:5000/api/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @services/menu_delete.json http://localhost:5000/api/change_menu_item
curl -X POST -H "Content-Type: application/json" -d @services/menu_adjust.json http://localhost:5000/api/change_menu_item
```
或是
```bash
curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADD", "restaurant_id": "restaurant001", "category": "Main Course", "item_name": "Spaghetti", "description": "Classic spaghetti with tomato sauce", "price": 10.99, "availability": true, "image_url": "https://example.com/spaghetti.jpg"}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "ADJUST", "item_name": "Spaghetti", "price": 12.99}' http://localhost:5000/change_menu_item

curl -X POST -H "Content-Type: application/json" -d '{"change_status": "DELETE", "item_name": "Spaghetti"}' http://localhost:5000/change_menu_item
```
=======

## System


### Kubernetes Setup
This project utilizes Kubernetes for deployment. The configuration files for the Kubernetes deployment reside within the kubernetes/backend and kubernetes/frontend directories.

### Before Deployment:

Image Tag Replacement: Locate the placeholder <IMAGE_TAG> within the deployment YAML files. Substitute it with the actual tag of your desired Docker image for deployment.
Deployment:
These commands will establish the essential Kubernetes resources (e.g., pods, services) required for the application.
 ```bash
 cd  meal_provider_2024
```

Run the following commands to initiate deployment:

#### database
```bash
kubectl apply -f kubernetes/database/secret.yaml
kubectl apply -f kubernetes/database/configmap.yaml
kubectl apply -f kubernetes/database/postgres-pvc.yaml
kubectl apply -f kubernetes/database/statefulset.yaml
kubectl apply -f kubernetes/database/svc-db.yaml
kubectl apply -f kubernetes/database/deploy-redis.yaml

```
#### Backend 

```bash
kubectl apply -f kubernetes/backend/deploy-backend.yaml --validate=false
kubectl apply -f kubernetes/backend/svc-backend.yaml --validate=false
```
#### Frontend 

```bash
kubectl apply -f kubernetes/frontend/deploy-frontend.yaml --validate=false
kubectl apply -f kubernetes/frontend/svc-frontend.yaml --validate=false
```

#### ingress

```bash
kubectl apply -f kubernetes/ingress.yaml
```

