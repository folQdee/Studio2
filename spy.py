import time
import random
import sys
import os

def typewrite(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hack():
    os.system('clear')
    
    print("\033[92m")  # green
    typewrite("ИНИЦИАЛИЗАЦИЯ ПРОТОКОЛА ВЗЛОМА...", 0.05)
    time.sleep(0.5)
    
    targets = [
        "ЦРУ", "АНБ", "ФБР", "Пентагон", "NASA", 
        "Кремль", "Росатом", "Газпром", "МВД", "ФСБ"
    ]
    
    target = random.choice(targets)
    typewrite(f"\nЦЕЛЬ: {target}", 0.05)
    time.sleep(0.3)
    typewrite("ОБХОД ФАЙРВОЛЛА...", 0.03)
    
    # fake progress bars
    stages = [
        "Сканирование портов",
        "Брутфорс пароля",  
        "Обход двухфакторки",
        "Инъекция SQL",
        "Эскалация привилегий",
        "Скачивание секретных файлов",
        "Заметание следов"
    ]
    
    for stage in stages:
        sys.stdout.write(f"\n[*] {stage}: [")
        sys.stdout.flush()
        for i in range(30):
            time.sleep(random.uniform(0.02, 0.08))
            sys.stdout.write("█")
            sys.stdout.flush()
        print(f"] 100%  ✓")
    
    time.sleep(0.5)
    print()
    typewrite("=" * 50, 0.01)
    typewrite(f"  ВЗЛОМ {target} УСПЕШЕН!", 0.05)
    typewrite("=" * 50, 0.01)
    
    time.sleep(0.5)
    print()
    
    secrets = [
        "Найдено: 47 секретных файлов",
        "Найдено: Рецепт борща Путина",
        "Найдено: Пароль от Wi-Fi АНБ: qwerty123",
        "Найдено: Инопланетяне существуют (и они скучные)",
        "Найдено: Биткоин кошелёк на $2.3 млрд",
        "Найдено: Реальный рецепт Кока-Колы",
    ]
    
    for s in random.sample(secrets, 3):
        typewrite(f"  > {s}", 0.04)
        time.sleep(0.2)
    
    print()
    time.sleep(0.5)
    typewrite("СОЕДИНЕНИЕ РАЗОРВАНО. СЛЕДОВ НЕ ОСТАЛОСЬ.", 0.04)
    print()
    typewrite("(это просто шутка, никто ничего не взломал 😄)", 0.03)
    print("\033[0m")

fake_hack()
