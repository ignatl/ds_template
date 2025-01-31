import subprocess
import sys
from pathlib import Path

def install_uv():
    try:
        # Install uv using curl
        subprocess.run([
            "curl",
            "-LsSf",
            "https://astral.sh/uv/install.sh",
            "|",
            "sh"
        ], check=True)
        
        print("✅ Successfully installed uv")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to install uv")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_uv()
