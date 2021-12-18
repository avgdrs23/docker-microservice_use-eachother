#!/bin/sh

#image=$(basename $PWD)
docker build -t app1:latest -f Dockerfile1 .
docker build -t app2:latest -f Dockerfile2 .
#Build two Images


