#!/usr/bin/env bash
# This Programm Write by Mr.nope
# SMS Sender v1.3.1
if [[ "$(id -u)" -ne 0 ]];
then
  echo "
Please, Run This Programm as Root!
"
  exit 1
fi
function main() {
    printf '\033]2;Sms-Sender/Installing'
    clear
    echo "Installing..."
    chmod +x smssender.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    echo "
Finish...!

Usage:
     python3 smssender.py
    "
    exit 1
}
main