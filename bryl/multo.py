import time
import sys

def animate_text(text, color_code="97", delay=0.09):
    for char in text:
        sys.stdout.write(f"\033[1;{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyrics():
    intro = "MULTO☕"
    animate_text(intro, color_code="95", delay=0.07)
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
        if line.strip() == "":
            time.sleep(1.5)
        else:
            if "multo" in line.lower():
                line_color = "96"
                delay = 0.1
            else:
                line_color = "97"
                delay = 0.09
            animate_text(line, color_code=line_color, delay=delay)
            time.sleep(0.5)

    print(f"\033[1;97m{'💔' * 1}\033[0m")
    time.sleep(0.5)

if __name__ == "__main__":
    sing_lyrics()
