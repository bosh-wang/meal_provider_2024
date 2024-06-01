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
### Run Flask server
```shell
cd backend/app
python main.py
```
#### api server will run on `localhost:5000`
