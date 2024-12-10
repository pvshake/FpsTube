FROM node:22.8.0-slim 

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN npm install

RUN chmod +x ./start.sh

CMD ["./start.sh"]