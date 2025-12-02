def term(n: int) -> float:
    return 1.0 + 1.0 / n


def main():
    # Дано a (1 < a <= 1.5).
    # Найти наименьшее n, такое что в последовательности
    # 1+1/2, 1+1/3, ..., 1+1/n последнее число будет меньше a.
    a = float(input())
    n = 2
    while True:
        if term(n) < a:
            print(n)
            break
        n += 1


if __name__ == "__main__":
    main()
