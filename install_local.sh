#!/bin/bash
set -e
set -x

# Instalar el servidor
pushd server
python setup.py install
popd

# Instalar el cliente
pushd client
python setup.py install
popd

echo "Server y Client instalados localmente."
