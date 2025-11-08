# syntax=docker/dockerfile:1.7

FROM python:3.14-slim
LABEL maintainer="Jorge Obiols <jorge.obiols@gmail.com>" \
      license="GPLv3" \
      description="WDB server with Python 3.13 compatibility."

ARG WDB_VERSION="3.3.2"

# Dependencias mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
      git \
      build-essential \
    && rm -rf /var/lib/apt/lists/*

# Clonamos usando secret para no dejar el token en la imagen
RUN --mount=type=secret,id=GITHUB_TOKEN \
    git clone https://$(cat /run/secrets/GITHUB_TOKEN)@github.com/quilsoft-org/wdb.git /opt/wdb \
    && pip install /opt/wdb/client \
    && pip install /opt/wdb/server \
    && rm -rf /opt/wdb

EXPOSE 19840
EXPOSE 1984

CMD ["wdb.server.py", "--detached_session", "--debug", "--more"]
