import os
import sys
import subprocess

# ANSI color codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


HEADER = r"""
$$$$$$$\  $$$$$$$\ $$\     $$\ $$\             $$$$$$\  $$$$$$\        $$$$$$$\   $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\\$$\   $$  |$$ |            \_$$  _|$$  __$$\       $$  __$$\ $$  __$$\\__$$  __|
$$ |  $$ |$$ |  $$ |\$$\ $$  / $$ |              $$ |  $$ /  \__|      $$ |  $$ |$$ /  $$ |  $$ |   
$$$$$$$\ |$$$$$$$  | \$$$$  /  $$ |              $$ |  \$$$$$$\        $$$$$$$\ |$$ |  $$ |  $$ |   
$$  __$$\ $$  __$$<   \$$  /   $$ |              $$ |   \____$$\       $$  __$$\ $$ |  $$ |  $$ |   
$$ |  $$ |$$ |  $$ |   $$ |    $$ |              $$ |  $$\   $$ |      $$ |  $$ |$$ |  $$ |  $$ |   
$$$$$$$  |$$ |  $$ |   $$ |    $$$$$$$$\       $$$$$$\ \$$$$$$  |      $$$$$$$  | $$$$$$  |  $$ |   
\_______/ \__|  \__|   \__|    \________|      \______| \______/       \_______/  \______/   \__|                                                                                                       
"""


def list_python_files(directory):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(".py")]
        return files
    except FileNotFoundError:
        print(Color.RED + f"❌ Folder '{directory}' not found." + Color.RESET)
        sys.exit(1)


def main():
    print(Color.GREEN + Color.BOLD + HEADER + Color.RESET)

    folder = "bryl"
    files = list_python_files(folder)

    if not files:
        print(Color.YELLOW + "⚠️ No Python files found in 'bryl/' folder." + Color.RESET)
        return

    print(Color.CYAN + "\nAvailable Python files:\n" + Color.RESET)

    for i, file in enumerate(files, start=1):
        print(f"{Color.WHITE}[{i}] {file}{Color.RESET}")

    try:
        choice = int(input(Color.GREEN + "\nEnter number to run: " + Color.RESET)) - 1

        if 0 <= choice < len(files):
            selected_file = os.path.join(folder, files[choice])
            print(Color.BLUE + f"\nRunning ☕: {files[choice]}\n" + Color.RESET)
            subprocess.run(["python", selected_file])
        else:
            print(Color.RED + "❌ Invalid choice." + Color.RESET)

    except ValueError:
        print(Color.RED + "❌ Please enter a valid number." + Color.RESET)


if __name__ == "__main__":
    main()
