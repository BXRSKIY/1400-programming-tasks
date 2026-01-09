import random

def main():
    # 10.1. Получить и вывести разные наборы случайных вещественных чисел.
    # Формат ввода:
    # k          (для пункта б)
    # a b        (для пункта д)
    # m a2 b2    (для пункта ж)
    k = int(input().strip())
    a, b = map(float, input().split())
    m, a2, b2 = input().split()
    m = int(m)
    a2 = float(a2)
    b2 = float(b2)

    # а) 8 случайных вещественных чисел ni (0 ≤ ni < 1)
    for _ in range(8):
        print(random.random())

    # б) k случайных вещественных чисел ni (0 ≤ ni < 1)
    for _ in range(k):
        print(random.random())

    # в) 15 случайных вещественных чисел ni (25 ≤ ni < 26)
    for _ in range(15):
        print(25.0 + random.random())

    # г) 20 случайных вещественных чисел ni (0 ≤ ni < 15)
    for _ in range(20):
        print(random.random() * 15.0)

    # д) случайное натуральное число k, не превосходящее a,
    # и k случайных вещественных чисел ni (0 ≤ ni < b)
    ra = int(a)
    if ra < 1:
        ra = 1
    k2 = random.randint(1, ra)
    print("k2 =", k2)
    for _ in range(k2):
        print(random.random() * b)

    # е) 10 случайных вещественных чисел ni (–40 ≤ ni < 40)
    for _ in range(10):
        print(random.uniform(-40.0, 40.0))

    # ж) случайное натуральное число k, не превосходящее m,
    # и k случайных вещественных чисел ni (a2 ≤ ni < b2)
    if m < 1:
        m = 1
    k3 = random.randint(1, m)
    print("k3 =", k3)
    for _ in range(k3):
        print(random.uniform(a2, b2))


if __name__ == "__main__":
    main()
