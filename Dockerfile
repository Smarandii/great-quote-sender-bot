FROM python:latest

RUN mkdir -p /usr/src/great-quote-sender-bot
WORKDIR /usr/src/great-quote-sender-bot

COPY . /usr/src/great-quote-sender-bot
RUN pip install -r requirements.txt
ENV API_TOKEN=ТВОЙ ТОКЕН ТУТ
CMD ["python3", "main.py"]