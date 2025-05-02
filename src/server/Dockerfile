FROM python:3

ARG WDB_VERSION="3.3.1"

RUN pip install git+https://github.com/jobiols/wdb.git@v3.3.1#egg=wdb.server&subdirectory=src/server

EXPOSE 19840
EXPOSE 1984
CMD ["wdb.server.py", "--detached_session"]
