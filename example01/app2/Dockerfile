FROM python:3

MAINTAINER Guilherme Amaral "guilherme.amaral@gmail.com"

COPY  ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT ["python"]

CMD ["app2.py"]
