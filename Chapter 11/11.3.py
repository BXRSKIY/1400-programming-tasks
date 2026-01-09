import random

def main():
    # 11.3. Заполнить массив из 15 элементов случайным образом:
    # а) вещественными значениями в [0,1);
    # б) вещественными значениями x (22 ≤ x < 23);
    # в) вещественными значениями x (0 ≤ x < 10);
    # г) вещественными значениями x (–50 ≤ x < 50);
    # д) целыми значениями в [0,10].
    n = 15

    print("a)")
    a = [random.random() for _ in range(n)]
    print(*a)

    print("b)")
    b = [22.0 + random.random() for _ in range(n)]
    print(*b)

    print("c)")
    c = [random.random() * 10.0 for _ in range(n)]
    print(*c)

    print("d)")
    d = [random.uniform(-50.0, 50.0) for _ in range(n)]
    print(*d)

    print("e)")
    e = [random.randint(0, 10) for _ in range(n)]
    print(*e)


if __name__ == "__main__":
    main()
