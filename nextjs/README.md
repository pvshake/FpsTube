# Projeto Final de Sistemas Distribuídos - Plataforma de streaming de vídeos

## Descrição

Front-End com Next.js do FpsTube

## Rodar a aplicação

Suba o container do Next.js caso não tenha feito na Root:

```bash
docker-compose up -d
```

Entre no container do Django:

```bash
docker-compose exec nextjs bash
```

Instale as dependências:

```bash
npm install
```

Rode a aplicação:

```bash
npm run dev
```

Acesse a aplicação em [http://localhost:3000](http://localhost:3000).
