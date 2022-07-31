#!/bin/bash
mkdir ubuntu_in_docker
cd ubuntu_in_docker
touch Dockerfile
echo "From ubuntu" > Dockerfile
docker build -t ubuntu_in_docker .
docker run -td ubuntu-os
id=$(docker ps | awk 'FNR == 2  {print $1}')
docker cp $id:/var/log .
docker rm -f $(docker ps -a -q)
echo "Dockerlar silinmiştir"
cd  ubuntu_in_docker
cp -r log/ ..
cd ..
rm -rf ubuntu_in_docker/

