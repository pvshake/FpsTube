FROM python:3.12.6-slim

ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONFAULTHANDLER 1 # Makes Python more verbose in case of an error

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools wheel

RUN pip install -r requirements.txt

RUN chmod +x ./start.sh
CMD ["./start.sh"]