#!/bin/bash
echo "mysql-starting"
docker pull mysql/mysql-server:latest
docker images
docker run --name=[user-doc] -d mysql/mysql-server:latest
docker ps
echo "starting-connect"
sudo apt install mysql-client
docker exec -it [user-doc] mysql -uroot -p
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '[qwerty]';

