import subprocess
import sys

try:
    subprocess.run(["cmatrix", "-b", "-u", "3"], check=True)
except FileNotFoundError:
    print("cmatrix не установлен, попробуй: sudo apt install cmatrix")
except KeyboardInterrupt:
    print("\nДобро пожаловать в реальный мир, Нео 🐇")
