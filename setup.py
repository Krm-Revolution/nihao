import os
import re
import sys
import subprocess

def extract_imports_from_file(filepath):
    imports = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'^\s*(import|from)\s+([a-zA-Z0-9_]+)', line)
            if match:
                module = match.group(2)
                # Skip standard library modules (basic filtering)
                if module not in sys.builtin_module_names:
                    imports.add(module)
    return imports

def collect_requirements_from_folder(folder):
    all_imports = set()
    if not os.path.exists(folder):
        print(f"❌ Folder '{folder}' not found.")
        return []

    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            filepath = os.path.join(folder, filename)
            all_imports.update(extract_imports_from_file(filepath))
    return list(all_imports)

def install_packages(packages):
    if not packages:
        print("📦 No third-party packages to install.")
        return
    print(f"📦 Installing packages: {', '.join(packages)}")
    subprocess.run(["pip", "install", *packages])

def run_setup():
    print("🔧 Updating Termux packages...")
    os.system("pkg update -y && pkg upgrade -y")

    print("🐍 Installing Python...")
    os.system("pkg install -y python")

    print("📦 Upgrading pip...")
    os.system("pip install --upgrade pip")

    print("🔍 Scanning Python files in 'bryl/' for dependencies...")
    packages = collect_requirements_from_folder("bryl")
    install_packages(packages)

    print("✅ Setup complete! You can now run your Python scripts.")

if __name__ == "__main__":
    run_setup()
