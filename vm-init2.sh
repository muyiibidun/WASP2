#!/bin/sh

# set hostname 
sudo echo “waspymq” > /etc/hostname

# Install some packages
sudo apt-get -y update
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip

# Install RABBITMQ
# insert rabbitmq APT repo to local source list
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list

# add rabbitmq keys to trusted key list 
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

# update package list
sudo apt-get -y update

# install rabbitmq package
sudo apt-get install -y rabbitmq-server

# stop and start
sudo rabbitmqctl stop
sudo rabbitmq-server start &

# running test hello-world program
sudo apt-get install python-pika

# prepare directory 
mkdir /usr/local/rabbitmq-test
cd /usr/local/rabbitmq-test

# echo "Cloning repo with WASPY2"
git clone https://github.com/muyiibidun/WASP2.git
