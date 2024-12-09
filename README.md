# Projeto Final Sistemas Distribuídos - FpsTube - Plataforma de streaming de vídeos

## Requerimentos

Cada projeto/pasta tem seus próprios requerimentos, mas uma ferramenta é comum a todos: o Docker.

### Docker

Você pode instalar o Docker Desktop primeiramente

Para rodar no Windows, use WSL para facilitar tudo

## Rodar a aplicação

Crie um volume docker com o nome `external-storage` que será compartilhado entre todos os serviços:

```bash
docker volume create external-storage
```

Rode todas as aplicações com o comando:

```bash
docker-compose up -d
```

Este comando irá subir todos os containers necessários para rodar todo o projeto

Acesse as pastas `golang`, `django` e `nextjs` e siga as instruções.

## Arquitetura do projeto

![alt text](./arquitetura_projeto.png)
