FROM python:3.12.6-slim

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools wheel

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg git bash -y

RUN chmod +x ./start.sh

CMD ["./start.sh"]