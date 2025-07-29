import os
import sys
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

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
        files = [f for f in os.listdir(directory) if f.endswith('.py')]
        return files
    except FileNotFoundError:
        print(Fore.RED + f"❌ Folder '{directory}' not found.")
        sys.exit(1)

def main():
    print(Fore.GREEN + Style.BRIGHT + HEADER)

    folder = "bryl"
    files = list_python_files(folder)

    if not files:
        print(Fore.YELLOW + "⚠️ No Python files found in 'bryl/' folder.")
        return

    print(Fore.CYAN + "\nAvailable Python files:\n")
    for i, file in enumerate(files, start=1):
        print(f"{Fore.WHITE}[{i}] {file}")

    try:
        choice = int(input(Fore.GREEN + "\nEnter number to run: ")) - 1
        if 0 <= choice < len(files):
            selected_file = os.path.join(folder, files[choice])
            print(Fore.BLUE + f"\nRunning ☕: {files[choice]}\n")
            subprocess.run(["python", selected_file])
        else:
            print(Fore.RED + "❌ Invalid choice.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
