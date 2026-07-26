import subprocess
import sys

try:
    subprocess.run(["curl", "parrot.live"], check=True)
except KeyboardInterrupt:
    print("\nПопугай устал танцевать 😴")
except Exception as e:
    print(f"Ошибка: {e}")
