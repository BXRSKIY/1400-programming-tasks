def term(n: int) -> float:
    return 1.0 + 1.0 / n


def main():
    # Дано a (1 < a <= 1.5).
    # Среди чисел 1+1/2, 1+1/3, ... найти первое, меньшее a.
    a = float(input())
    n = 2
    while True:
        t = term(n)
        if t < a:
            print(t)
            break
        n += 1


if __name__ == "__main__":
    main()
