FROM python:3.14-alpine
LABEL maintainer="Jorge Obiols <jorge.obiols@gmail.com>" \
      license="GPLv3" \
      description="Fork of WDB with improvements and Python 3.13 compatibility. Based on the original project by Florian Mounier (Kozea)."

ARG CACHEBUST=1
ARG WDB_VERSION="3.3.2"

RUN apk update && apk add --no-cache git

RUN git clone https://${GITHUB_TOKEN}@github.com/quilsoft-org/wdb.git /opt/wdb \
    && pip install /opt/wdb/client \
    && pip install /opt/wdb/server

EXPOSE 19840
EXPOSE 1984
CMD ["wdb.server.py", "--detached_session", "--debug", "--more"]
