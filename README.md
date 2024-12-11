# Projeto Final Sistemas Distribuídos - FpsTube - Plataforma de streaming de vídeos

## Requerimentos

Cada projeto/pasta tem seus próprios requerimentos, mas uma ferramenta é comum a todos: o Docker.

### Docker

Você pode instalar o Docker Desktop primeiramente

Para rodar no Windows, use WSL para facilitar tudo

## Rodar a aplicação

Antes de tudo, abra o Docker desktop e caso já tenha rodado alguma vez ou para ter certeza que não possui nada criado, rode os comandos no terminal do vscode ou outra IDE:

```bash
docker system prune --all
```

e

```bash
docker volume prune -f
```

Crie um volume docker com o nome `external-storage` que será compartilhado entre todos os serviços:

```bash
docker volume create external-storage
```

Rode todas as aplicações com o comando:

```bash
docker-compose up —force-recreate -d
```

Este comando irá subir todos os containers necessários para rodar todo o projeto

Acesse as pastas `engine`, `django` e `nextjs` e siga as instruções.

## Arquitetura do projeto

![alt text](./arquitetura_projeto.png)
