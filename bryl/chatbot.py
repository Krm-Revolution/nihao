import requests
import time
import sys
from colorama import init, Fore, Style

init()

def matrix_print(text):
    colors = [Fore.GREEN, Fore.LIGHTGREEN_EX]
    for char in text:
        color = colors[int(time.time() * 10) % 2]
        sys.stdout.write(color + Style.BRIGHT + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def chat():
    print(Fore.GREEN + Style.BRIGHT + "CHAT MO SI BRYL\nPLS (Type 0 to exit)" + Style.RESET_ALL)

    while True:
        user_input = input(Fore.WHITE + "You: ")
        if user_input == "0":
            matrix_print("\nBRYL: SO LONG MY PREND💔!!")
            break

        try:
            response = requests.get(f"https://yq-cloud.vercel.app/chat?q={user_input}").json()
            sys.stdout.write(Fore.GREEN + "BRYL: " + Style.BRIGHT)
            matrix_print(response['response'])
        except:
            matrix_print("BRYL: Connection failed, try again...")

if __name__ == "__main__":
    chat()
