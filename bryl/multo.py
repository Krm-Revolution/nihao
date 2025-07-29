import time
import sys
from colorama import init, Fore, Style

init()

def animate_text(text, color=Fore.WHITE, delay=0.09):
    """Animates text one character at a time with the specified color."""
    for char in text:
        sys.stdout.write(color + Style.BRIGHT + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyrics():
    # 
    intro = "MULTO☕"
    animate_text(intro, color=Fore.MAGENTA, delay=0.07)
    time.sleep(1)

    lyrics = [
        "Hindi na makalaya",
        "Dinadalaw mo 'ko bawat gabi",
        "Wala mang nakikita",
        "Haplos mo'y ramdam pa rin sa dilim",
        "",
        "Hindi na nananaginip",
        "Hindi na ma-makagising",
        "Pasindi na ng ilaw",
        "Minumulto na 'ko ng damdamin ko",
        "Ng damdamin ko"
    ]

    for line in lyrics:
        # 
        if line.strip() == "":
            time.sleep(1.5)
        else:
            # 
            if "multo" in line.lower():
                line_color = Fore.CYAN  # 
                delay = 0.1  # 
            else:
                line_color = Fore.WHITE
                delay = 0.09
            animate_text(line, color=line_color, delay=delay)
            # 
            time.sleep(0.5)

    # 
    print(Fore.WHITE + Style.BRIGHT + "💔" * 1 + Style.RESET_ALL)
    time.sleep(0.5)

if __name__ == "__main__":
    sing_lyrics()
