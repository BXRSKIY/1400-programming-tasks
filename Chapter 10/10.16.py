import random

def main():
    # 10.16. Случайный выбор одной кости домино из полного набора 0-0..6-6.
    # Представим кость как (a,b) с 0<=a<=b<=6.
    # Сгенерируем случайную пару по индексу.
    tiles = []
    for a in range(0, 7):
        for b in range(a, 7):
            tiles.append((a, b))
    t = random.choice(tiles)
    print(f"Выбрана кость {t[0]}-{t[1]}")


if __name__ == "__main__":
    main()
