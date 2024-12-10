# Utilizando uma imagem oficial do Golang para desenvolvimento
FROM golang:1.23-alpine

# Instalação de ferramentas adicionais como git e ca-certificates
RUN apk add --no-cache git bash ffmpeg

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo go.mod e go.sum para dentro do container
ADD . /app/

RUN go mod download

RUN chmod +x ./start.sh
CMD ["./start.sh"]