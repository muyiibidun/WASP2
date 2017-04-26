#!/bin/sh

# set hostname 
sudo echo waspmq > /etc/hostname
sudo sed -i "s/127.0.0.1 localhost/127.0.0.1 waspmq/g" /etc/hosts

# Install some packages
sudo apt-get -y update
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip


#Install Erlang (the RabbitMQ runtime)--download and add Erlang to APT repository
sudo wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
sudo dpkg -i erlang-solutions_1.0_all.deb
sudo apt-get update

#Install Erlang
sudo apt-get -y install socat erlang-nox=1:19.3-1

#Download the official RabbitMQ 3.6.9 .deb installer package (check the official installation guide for more: http://www.rabbitmq.com/install-debian.html)
sudo wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-server_3.6.9-1_all.deb

#Install the package using dpkg
sudo dpkg -i rabbitmq-server_3.6.9-1_all.deb


# enable the RabbitMQ service
sudo update-rc.d rabbitmq-server enable


#Start  the RabbitMQ service 
sudo service rabbitmq-server start

#To stop the service use the command
# sudo service rabbitmq-server stop

# Install python pika 
sudo apt-get install -y python-pika

# create users and set privileges to enable remote connection
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"


