#!/bin/bash 

#docker run  -it $1:latest
#Run your Docker Image

docker run -d  --network=host app2
docker run -d  --network=host app1
# --network - means to connect the container host
