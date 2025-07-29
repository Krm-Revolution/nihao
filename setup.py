import os

def run_setup():
    print("🔧 Updating Termux packages...")
    os.system("pkg update -y && pkg upgrade -y")

    print("🐍 Installing Python and pip...")
    os.system("pkg install -y python")

    print("📦 Installing required Python packages...")
    os.system("pip install --upgrade pip")
    os.system("pip install colorama requests")

    print("✅ Setup complete! You can now run your Python scripts.")

if __name__ == "__main__":
    run_setup()
