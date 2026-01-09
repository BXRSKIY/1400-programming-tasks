import random

def main():
    # 10.23. Вариант 10.20 с козырной мастью.
    suits = ["пики", "трефы", "бубны", "червы"]
    ranks = ["шестерка", "семерка", "восьмерка", "девятка",
             "десятка", "валет", "дама", "король", "туз"]
    trump = random.choice(suits)
    s = random.choice(suits)
    r = random.choice(ranks)
    print(f"Козырная масть: {trump}")
    print(f"Выбрана карта: {r} {s}")


if __name__ == "__main__":
    main()
