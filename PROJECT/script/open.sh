#!/bin/bash
mkdir ubuntu_in_docker
cd ubuntu_in_docker
touch Dockerfile
echo "From ubuntu" > Dockerfile
docker build -t ubuntu_in_docker .
docker run -td ubuntu-os
