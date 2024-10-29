# Utilizando uma imagem oficial do Golang para desenvolvimento
FROM golang:1.23-alpine

# Instalação de ferramentas adicionais como git e ca-certificates
RUN apk add --no-cache bash ffmpeg

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o restante dos arquivos da aplicação para dentro do container
COPY . .

# Definir o ponto de entrada (entrypoint) como bash para que você possa interagir
CMD [ "bash" ]
