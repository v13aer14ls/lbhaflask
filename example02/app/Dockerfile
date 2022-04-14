FROM python:alpine

MAINTAINER Guilherme Amaral "guilherme.amaral@gmail.com"

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

CMD python app.py
