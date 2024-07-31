import os
import sys
import random
import asyncio
import aiohttp
import colorama
from colorama import Fore, Style, init
import subprocess
import time
import string
import requests
import re
import threading
import discord
from discord.ext import commands

if os.name == 'nt':
    os.system('title NuxiBackup-Tool |  Outil réalisé par Nux!Backup/frn')

exit_event = asyncio.Event()
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    clear_screen()

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    print(f"""
                         {RED}▐ ▄ ▄• ▄▌▐▄• ▄ ▪  ▄▄▄▄·  ▄▄▄·  ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·  ▄▄▄▄▄▄            ▄▄▌  
                        •█▌▐██▪██▌ █▌█▌▪██ ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█  ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  
                        ▐█▐▐▌█▌▐█▌ ·██· ▐█·▐█▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
                        ██▐█▌▐█▄█▌▪▐█·█▌▐█▌██▄▪▐█▐█▪ ▐▌▐███▌▐█.█▌▐█▄█▌▐█▪·•    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
                        ▀▀ █▪ ▀▀▀ •▀▀ ▀▀▀▀▀·▀▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀       ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
                                            | Outil réalisé par Nux!Backup/frn |
                                                    | Menu Principal |
{RESET}          
               [{RED}1{RESET}] {RED}->{RESET} {WHITE}Configuration IP{RESET}          [{RED}6{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}11{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}16{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET} 
               [{RED}2{RESET}] {RED}->{RESET} {WHITE}Ping une adresse IP{RESET}       [{RED}7{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}12{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}17{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}
               [{RED}3{RESET}] {RED}->{RESET} {WHITE}Générer du code Nitro{RESET}     [{RED}8{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}13{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}18{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}
               [{RED}4{RESET}] {RED}->{RESET} {WHITE}Informations sur l'outil{RESET}  [{RED}9{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}14{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}19{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}
               [{RED}5{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}                   [{RED}10{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}         [{RED}15{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}          [{RED}20{RESET}] {RED}->{RESET} {WHITE}Soon...{RESET}
    """)

def ip_config():
    clear_screen()

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    
    print(f"""
                         {RED}▐ ▄ ▄• ▄▌▐▄• ▄ ▪  ▄▄▄▄·  ▄▄▄·  ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·  ▄▄▄▄▄▄            ▄▄▌  
                        •█▌▐██▪██▌ █▌█▌▪██ ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█  ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  
                        ▐█▐▐▌█▌▐█▌ ·██· ▐█·▐█▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
                        ██▐█▌▐█▄█▌▪▐█·█▌▐█▌██▄▪▐█▐█▪ ▐▌▐███▌▐█.█▌▐█▄█▌▐█▪·•    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
                        ▀▀ █▪ ▀▀▀ •▀▀ ▀▀▀▀▀·▀▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀       ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
                                            | Outil réalisé par Nux!Backup/frn |
                                                   | Configuration IP |
                        """)
    os.system(f"ipconfig")
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def ping_an_ip_address():
    clear_screen()

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    print(f"""
                         {RED}▐ ▄ ▄• ▄▌▐▄• ▄ ▪  ▄▄▄▄·  ▄▄▄·  ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·  ▄▄▄▄▄▄            ▄▄▌  
                        •█▌▐██▪██▌ █▌█▌▪██ ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█  ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  
                        ▐█▐▐▌█▌▐█▌ ·██· ▐█·▐█▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
                        ██▐█▌▐█▄█▌▪▐█·█▌▐█▌██▄▪▐█▐█▪ ▐▌▐███▌▐█.█▌▐█▄█▌▐█▪·•    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
                        ▀▀ █▪ ▀▀▀ •▀▀ ▀▀▀▀▀·▀▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀       ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
                                            | Outil réalisé par Nux!Backup/frn |
                                                  | Ping une adresse IP |
                        """)
    ip_address = input(f"{RED}Entrez une adresse IP ->{RESET}  ")
    os.system(f"ping {ip_address}")
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def generate_nitro_code():

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"{RED}https://discord.gift/{code}"

def invalid_option():

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    print(f"{RED}[x] Invalid Choice")
    time.sleep(1)
    display_main_menu()

def info_sur_loutil():
    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    print(f"""
                         {RED}▐ ▄ ▄• ▄▌▐▄• ▄ ▪  ▄▄▄▄·  ▄▄▄·  ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·  ▄▄▄▄▄▄            ▄▄▌  
                        •█▌▐██▪██▌ █▌█▌▪██ ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█  ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  
                        ▐█▐▐▌█▌▐█▌ ·██· ▐█·▐█▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
                        ██▐█▌▐█▄█▌▪▐█·█▌▐█▌██▄▪▐█▐█▪ ▐▌▐███▌▐█.█▌▐█▄█▌▐█▪·•    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
                        ▀▀ █▪ ▀▀▀ •▀▀ ▀▀▀▀▀·▀▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀       ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
                                            | Outil réalisé par Nux!Backup/frn |
                                                | Informations sur l'outil |
                    """)
    print(f"{RED}[+] Name : Nuxi")
    print(f"{RED}[+] Coding : Python")
    print(f"{RED}[+] Language : FR")
    print(f"{RED}[+] Creator : Nux!Backup/frn")
    print(f"{RED}[+] Discord : https://discord.gg/BC72e3z5cG")
    print(f"{RED}[+] GitHub : https://github.com/Nuh1x")
    input("\nAppuyez sur Entrée pour revenir au menu principal...") 


def main():

    RED = Fore.RED
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    while True:
        display_main_menu()
        option = input(f"""{RED}
┌───({RESET}User@nuxibackup-tool{RED})─[{RESET}~/NuxiBackup-Tool{RED}]
└──{RESET}$ """)
        if option == "1":
            ip_config()
        elif option == "2":
            ping_an_ip_address()            
        elif option == "3":
            generate_nitro_code()
            clear_screen()
            nitro_code = generate_nitro_code()
            print(f"""
                         {RED}▐ ▄ ▄• ▄▌▐▄• ▄ ▪  ▄▄▄▄·  ▄▄▄·  ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·  ▄▄▄▄▄▄            ▄▄▌  
                        •█▌▐██▪██▌ █▌█▌▪██ ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█  ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  
                        ▐█▐▐▌█▌▐█▌ ·██· ▐█·▐█▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
                        ██▐█▌▐█▄█▌▪▐█·█▌▐█▌██▄▪▐█▐█▪ ▐▌▐███▌▐█.█▌▐█▄█▌▐█▪·•    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
                        ▀▀ █▪ ▀▀▀ •▀▀ ▀▀▀▀▀·▀▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀       ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
                                            | Outil réalisé par Nux!Backup/frn |
                                                 | Générer du code Nitro |
                        """)
            print(f"{RED}[+] Code Nitro généré: {nitro_code}{RESET}")
            input("\nAppuyez sur Entrée pour revenir au menu principal...")
        elif option == "4":
            clear_screen()
            info_sur_loutil()
        elif option in {"5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}:
            invalid_option()

if __name__ == "__main__": 
    main()