#!/bin/bash
echo " EXPECT0"
#!/bin/bash
sudo apt-get update -y && sudo apt-get upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker [user_name]
sudo usermod -aG docker Pi
docker version
docker run hello-world
