# Projeto Final Sistemas Distribuidos - Plataforma de streaming de vídeos

## Descrição

Microsserviço em Go (conversor de vídeos)

## Rodar a aplicação

Levante os containers:

```bash
docker-compose up -d
```

Através do PGAdmin, crie as tabelas do arquivo `prepare-db.sql` no banco de dados `converter`.

Acesse o container o rodando o comando:

```bash
docker compose exec go_app_dev bash
```

Use os comandos `go run cmd/splitchunks/main.go` e `go run cmd/videoconverter/main.go` para rodar a aplicação.
