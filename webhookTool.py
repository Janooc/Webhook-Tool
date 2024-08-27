import time
import requests
import os
import threading
import asyncio
import aiohttp
from colorama import Fore
from pystyle import *

# Function to clear the console
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Webhook Spammer function
def webhook_spammer():
    clear()
    madeby = "Made by janooc"
    print(Colors.cyan, f"""
     ▄▄▄▄    ▄▄▄     ▄▄▄█████▓
    ▓█████▄ ▒████▄   ▓  ██▒ ▓▒
    ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░
    ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ 
    ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ 
    ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   
    ▒░▒   ░   ▒   ▒▒ ░   ░    
     ░    ░   ░   ▒    ░      
     ░            ░  ░        
          ░                   
    \n{madeby}
    """)

    webhook = input(f"{Fore.CYAN}Webhook:{Fore.RESET} ")
    webhookname = input(f"{Fore.CYAN}Webhook name:{Fore.RESET} ")
    sleep = input(f"{Fore.CYAN}Delay:{Fore.RESET} ")
    count = input(f"{Fore.CYAN}Request number:{Fore.RESET} ")
    message = input(f"{Fore.CYAN}Message:{Fore.RESET} ")
    threadingoption = input(f"{Fore.CYAN}Threading? [y/n]:{Fore.RESET} ")

    if threadingoption.lower() == "y":
        threadingoption = "True"
    else:
        threadingoption = "False"

    data = {
        "content" : message,
        "username" : webhookname
    }
    count = int(count)
    sleep = int(sleep)

    Write.Print("\nStarted spamming webhook!\n", Colors.cyan)
    print("")

    goodreqs = 0
    failedreqs = 0

    start_time = time.time()

    def spamwebhook():
        nonlocal goodreqs, failedreqs
        
        currenttime = time.strftime("%H:%M", time.localtime()) 
        time.sleep(sleep)
        response = requests.post(webhook, data=data)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+]{Fore.RESET} [{currenttime}] | Successful request sent!")
            goodreqs += 1
        else:
            print(f"{Fore.RED}[-]{Fore.RESET} [{currenttime}] Failed to send webhook {response.status_code}")
            failedreqs += 1

    if threadingoption == "True":
        threads = []

        for i in range(count):
            t = threading.Thread(target=spamwebhook)
            t.daemon = True
            threads.append(t)

        for i in range(count):
            threads[i].start()
            
        for i in range(count):
            threads[i].join()

    elif threadingoption == "False":
        for i in range(count):
            spamwebhook()

    end_time = time.time()
    elapsed_time = end_time - start_time

    Write.Print(f"\nFinished spamming webhook!\n", Colors.cyan)
    print(f"{Fore.CYAN}Successful requests:{Fore.RESET} {goodreqs}\n{Fore.CYAN}Failed requests:{Fore.RESET} {failedreqs}\n{Fore.CYAN}Elapsed time:{Fore.RESET} {elapsed_time:.2f} seconds\n")
    time.sleep(3)
    
# Webhook Deleter function
async def webhook_deleter():
    clear()
    madeby = "Made by janooc"
    print(Colors.cyan, f"""
     ▄▄▄▄    ▄▄▄     ▄▄▄█████▓
    ▓█████▄ ▒████▄   ▓  ██▒ ▓▒
    ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░
    ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ 
    ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ 
    ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   
    ▒░▒   ░   ▒   ▒▒ ░   ░    
     ░    ░   ░   ▒    ░      
     ░            ░  ░        
          ░                   
    \n{madeby}
    """)

    WEBHOOK_URL = input(str(f"{Fore.CYAN}Enter the webhook URL > {Fore.RESET}"))

    async with aiohttp.ClientSession() as session:
        async with session.delete(WEBHOOK_URL) as resp:
            if resp.status == 204:
                print(f'{Fore.GREEN}Webhook successfully deleted{Fore.RESET}')
                time.sleep(3)
            else:
                print(f'{Fore.RED}Failed to delete webhook.{Fore.RESET}')
                time.sleep(3)

    input(f"\n{Fore.CYAN}Press enter to leave the program...{Fore.RESET}")

# Main Menu function
def main_menu():
    while True:
        clear()
        print(Colors.cyan, f"""
        1. Webhook Spammer
        2. Webhook Deleter
        3. Exit
        """)
        choice = input(f"{Fore.CYAN}Choose an option:{Fore.RESET} ")

        if choice == "1":
            webhook_spammer()
        elif choice == "2":
            asyncio.run(webhook_deleter())
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Invalid option! Please try again.{Fore.RESET}")
            time.sleep(2)

main_menu()
