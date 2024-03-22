FROM python:3.10

WORKDIR /application

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./src src
COPY ./data data
COPY ./templates templates
COPY ./app.py app.py

CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "9001"]