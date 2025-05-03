#!/usr/bin/env bash
sudo docker build --rm=true -t jobiols/wdb:3.3.1 ./
sudo docker push jobiols/wdb:3.3.1
