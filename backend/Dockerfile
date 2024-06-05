FROM python:3.10.14-alpine3.18
 
WORKDIR /app
 
COPY . /app
 
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
 
CMD python /app/app/main.py