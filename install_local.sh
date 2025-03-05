#!/bin/bash
set -e
set -x

# Instalar el servidor
pushd server
python3 -m pip install .
popd

# Instalar el cliente
pushd client
python3 -m pip install .
popd

echo "Server y Client instalados localmente."
