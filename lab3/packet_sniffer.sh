#!/bin/bash
# script used for running sudo in pycharm venv
# printing out arguements
count=1
arguements=""
filename=packet_sniffer.py
for para in $@:
do
 echo arguement $count is $para
 arguements="${arguements} ${para}"
 count=$((count+1))
done
#for fun
echo arguements $arguements
#run the python script as sudo
sudo  /home/alex/PycharmProjects/SDN/lab3/venv/bin/python $filename $*
