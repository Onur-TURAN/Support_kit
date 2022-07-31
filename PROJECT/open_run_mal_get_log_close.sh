#!/bin/bash
mkdir ubuntu_in_docker
cd ubuntu_in_docker
touch Dockerfile
echo "From ubuntu" > Dockerfile
docker build -t ubuntu_in_docker .
docker run -td ubuntu-os
id=$(docker ps | awk 'FNR == 2  {print $1}')
echo "1"
docker cp ./$malware $id:/
echo "2"
docker exec $id  ./$malware
echo "3"
docker cp $id:/var/log .
echo "4"
docker rm -f $(docker ps -a -q)
cd  ubuntu_in_docker
cp -r log/ ..
cd ..
rm -rf ubuntu_in_docker/

