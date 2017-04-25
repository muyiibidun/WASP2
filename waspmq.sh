#!/bin/sh

# set hostname 
sudo echo waspmq > /etc/hostname
sudo sed -i "s/127.0.0.1 localhost/127.0.0.1 waspmq/g" /etc/hosts

# insert rabbitmq APT repo to local source list
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list

# add rabbitmq keys to trusted key list 
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

# install some dependencies
sudo apt-get -y update
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip

# install rabbitmq package
sudo apt-get install -y rabbitmq-server
sudo apt-get install -y python-pika

# create users and set privileges to enable remote connection
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"

# prepare directory 
mkdir /usr/local/rabbitmq-test
cd /usr/local/rabbitmq-test

# echo "Cloning repo with WASP2"
git clone https://github.com/muyiibidun/WASP2.git