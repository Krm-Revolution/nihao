import requests
import time
import sys

# ANSI color codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    GREEN = "\033[32m"
    LIGHT_GREEN = "\033[92m"
    WHITE = "\033[37m"


def matrix_print(text):
    colors = [Color.GREEN, Color.LIGHT_GREEN]

    for char in text:
        color = colors[int(time.time() * 10) % 2]
        sys.stdout.write(color + Color.BOLD + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.03)

    print()


def chat():
    print(Color.GREEN + Color.BOLD + "CHAT MO SI BRYL\nPLS (Type 0 to exit)" + Color.RESET)

    while True:
        user_input = input(Color.WHITE + "You: " + Color.RESET)

        if user_input == "0":
            matrix_print("\nBRYL: SO LONG MY PREND💔!!")
            break

        try:
            response = requests.get(
                f"https://yq-cloud.vercel.app/chat?q={user_input}"
            ).json()

            sys.stdout.write(Color.GREEN + "BRYL: " + Color.BOLD)
            matrix_print(response["response"])

        except Exception:
            matrix_print("BRYL: Connection failed, try again...")


if __name__ == "__main__":
    chat()
