FROM python:3.12.3
LABEL org.opencontainers.image.authors="Jorge Obiols <jorge.obiols@gmail.com>" \
      org.opencontainers.image.version="3.3.1" \
      org.opencontainers.image.description="Servidor WDB para depuración remota"

ARG WDB_VERSION="3.3.1"

RUN apt-get update && apt-get install -y git

RUN git clone -b main.try5 https://${GITHUB_TOKEN}@github.com/quilsoft-org/wdb.git /opt/wdb \
 && pip install /opt/wdb/server

EXPOSE 19840
EXPOSE 1984
CMD ["wdb.server.py", "--detached_session"]
