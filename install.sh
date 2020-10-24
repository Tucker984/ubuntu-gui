#!/bin/bash/
echo "installing perl"
sudo apt-get update
sudo apt-get install perl
echo "installing npm/nodejs"
sudo apt update
sudo apt install nodejs
sudo apt install npm
echo "installing python"
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt update
echo "installing pip"
sudo apt-get update
sudo apt-get -y install python3-pip
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
echo "installing xterm module"
npm install xterm
echo "installing python-tk"
sudo apt-get install python-tk
echo "installing SQLite3"
pip install bcrypt
echo "install complete"
