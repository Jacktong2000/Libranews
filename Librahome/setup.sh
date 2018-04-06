#! /usr/bin/env bash


'echo "set const" >> .nanorc'

'echo "set tabsize 4" >> .nanorc'

'echo "set tabstospaces" >> .nanorc'

sudo apt-get update
sudo apt-get install python3-pip
pip3 install flask
pip3 install selenium
pip3 install numpy
pip3 install pandas
