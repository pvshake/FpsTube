# Projeto Final Sistemas Distribuídos - Plataforma de streaming de vídeos

## Descrição

Backend Django (admin dos vídeos)

## Requerimentos

É necessário instalar o Python no Docker para não precisar instalar na máquina local

## Rodar a aplicação

Suba os containers se não fez na Root:

```bash
docker-compose up -d
```

Entre no container do Django:

```bash
docker-compose exec django bash
```

Rode as migrações do Django:

```bash
./manage.py migrate
```

Crie um superusuário:

```bash
./manage.py createsuperuser
```

Nesse mesmo terminal, chame o consumer 1 do RabbitMQ e fique monitorando:

```bash
./manage.py consumer_register_processed_video_path
```

Abra um 2º terminal ao lado, chame o consumer 2 do RabbitMQ e fique monitorando:

```bash
docker-compose exec django bash
```

```bash
./manage.py consumer_upload_chunks_to_external_storage
```

Acesse o admin em [http://localhost:8000/admin]().

## Configurar /etc/hosts

O RabbitMQ está sendo executado no `docker-compose.yaml` da aplicação Golang, assim como o Django está em outro `docker-compose.yaml`, os containers estão em redes diferentes.
Usaremos a estratégia do `host.docker.internal` para comunicação entre os containers.

Para isto é necessário configurar um endereços que todos os containers Docker consigam acessar.

Acrescente no seu /etc/hosts (para Windows o caminho é C:\Windows\system32\drivers\etc\hosts):

```
127.0.0.1 host.docker.internal
```

Em todos os sistemas operacionais é necessário abrir o programa para editar o _hosts_ como Administrator da máquina ou root.

Obs.: Se estiver usando o Docker Desktop, pode ser que o `host.docker.internal` já esteja configurado,então remova a linha do arquivo hosts e acrescente a recomendada acima.
