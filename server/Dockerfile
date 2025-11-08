# syntax=docker/dockerfile:1.7

FROM python:3.14-alpine
LABEL maintainer="Jorge Obiols <jorge.obiols@gmail.com>" \
      license="GPLv3" \
      description="Fork of WDB with improvements and Python 3.13 compatibility. Based on the original project by Florian Mounier (Kozea)."

ARG WDB_VERSION="3.3.2"

# Dependencias necesarias para compilar e instalar
RUN apk update && apk add --no-cache git python3-dev build-base

# Clonar wdb sin dejar el token en la imagen (BuildKit secret)
RUN --mount=type=secret,id=GITHUB_TOKEN \
    git clone https://$(cat /run/secrets/GITHUB_TOKEN)@github.com/quilsoft-org/wdb.git /opt/wdb \
    && pip install /opt/wdb/client \
    && pip install /opt/wdb/server \
    && rm -rf /opt/wdb

# Exponer puertos
EXPOSE 19840
EXPOSE 1984

CMD ["wdb.server.py", "--detached_session", "--debug", "--more"]
