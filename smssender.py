#!/usr/bin/python3
# This Programm Write by Mr.nope
# Sms-Sender v1.3.1
import os
import time
import sys
import webbrowser
import platform
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
try:
    from twilio.rest import Client
except ImportError:
    os.system("pip install twilio")
    from twilio.rest import Client
system = platform.uname()[0]
Run_Err = "\nPlease, Run This Programm on Linux, Windows or MacOS!\n"
banner = Fore.LIGHTGREEN_EX + """
          ________  
      (( /========\
      __/__________\____________n_
  (( /              \_____________] """ + Fore.RED + " [*] " + Fore.GREEN + "Version: " + Fore.YELLOW + "1.3.1" + Fore.LIGHTGREEN_EX + """
    /  =(*)=          \
    |_._._._._._._._._.|         !
(( / __________________ \       =o
  | OOOOOOOOOOOOOOOOOOO0 |   = \n""" + End
def title():
    if system == 'Linux':
        os.system("printf '\033]2;Sms-Sender\a'")
    elif system == 'Windows':
        os.system("title Sms-Sender")
    else:
        print(Run_Err)
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(Run_Err)
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    try1()
def try1():
    try_to_ch_tw = input("\nHave you created an account at supermetrics.com? [y/n] ")
    if try_to_ch_tw == 'y':
        try4()
    elif try_to_ch_tw == 'n':
        try3()
    else:
        try1()
def try3():
    print("\nOpenning supermetrics.com...")
    time.sleep(2)
    webbrowser.open_new_tab("https://team.supermetrics.com/")
    print("\n-----------------\n")
    try4()
def try4():
    cls()
    print(banner)
    number = input("\nEnter your Number: ")
    time.sleep(0.25)
    target = input("\nEnter Target number: ")
    time.sleep(2)
    try1()
    tocken = input("\nEnter tocken: ")
    time.sleep(0.80)
    tocken_2 = input("\n2: ")
    client = Client(tocken,tocken_2)
    time.sleep(0.25)
    mess = input("\nEnter Message: ")
    time.sleep(0.50)
    client.message.create(to=target,from_=number,body=mess)
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting... ;)")
        sys.exit()