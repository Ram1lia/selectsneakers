FROM python:latest

RUN mkdir /app1
WORKDIR /app1/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app1

CMD ["python", "manage.py runserver"]



