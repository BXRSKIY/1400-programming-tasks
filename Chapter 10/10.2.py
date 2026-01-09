import random

def main():
    # 10.2. Получить и вывести случайные целые числа в заданных диапазонах.
    # Формат ввода:
    # k a        (для пункта б)
    # k2 a2      (для пункта г)
    # a3 b3      (для пункта д)
    k, a = map(int, input().split())
    k2, a2 = map(int, input().split())
    a3, b3 = map(int, input().split())

    # а) 10 случайных целых чисел в [0, 10]
    for _ in range(10):
        print(random.randint(0, 10))

    # б) k случайных целых чисел в [0, a]
    for _ in range(k):
        print(random.randint(0, a))

    # в) 20 случайных целых чисел в [10, 20]
    for _ in range(20):
        print(random.randint(10, 20))

    # г) k2 случайных целых чисел в [-10, a2]
    for _ in range(k2):
        print(random.randint(-10, a2))

    # д) случайное натуральное k, не превосходящее 15,
    # и k случайных целых чисел в [a3, b3]
    k3 = random.randint(1, 15)
    print("k3 =", k3)
    for _ in range(k3):
        print(random.randint(a3, b3))


if __name__ == "__main__":
    main()
