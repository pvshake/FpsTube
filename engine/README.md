# Projeto Final Sistemas Distribuidos - Plataforma de streaming de vídeos

## Descrição

Microsserviço em Python (conversor de vídeos)

## Rodar a aplicação

Suba os containers se não fez na Root:

```bash
docker-compose up -d
```

Para acessar o container, rode o comando:

```bash
docker compose exec engine bash
```

Em um 3º terminal, acompanhe os logs da comunicação do RabbitMQ entre os serviços:

```bash
docker-compose logs engine --follow
```
