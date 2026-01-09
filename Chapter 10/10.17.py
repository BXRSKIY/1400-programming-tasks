import random

def main():
    # 10.17. Выбор двух костей домино из полного набора и проверка,
    # можно ли их приложить друг к другу.
    tiles = []
    for a in range(0, 7):
        for b in range(a, 7):
            tiles.append((a, b))
    t1 = random.choice(tiles)
    tiles2 = tiles.copy()
    tiles2.remove(t1)
    t2 = random.choice(tiles2)
    print(f"Кость 1: {t1[0]}-{t1[1]}")
    print(f"Кость 2: {t2[0]}-{t2[1]}")
    # Можно ли приложить: у них есть общая цифра
    can = (t1[0] == t2[0] or t1[0] == t2[1] or
           t1[1] == t2[0] or t1[1] == t2[1])
    if can:
        print("Кости можно приложить друг к другу.")
    else:
        print("Кости приложить нельзя.")


if __name__ == "__main__":
    main()
