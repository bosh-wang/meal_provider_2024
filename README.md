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