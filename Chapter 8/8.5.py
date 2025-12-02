def term(n: int) -> float:
    return 1.0 + 1.0 / n  # n >= 2


def main():
    # Дано a (1 < a <= 1.5).
    # Из чисел 1+1/2, 1+1/3, 1+1/4, ... напечатать те, которые не меньше a.
    a = float(input())
    n = 2
    while True:
        t = term(n)
        if t >= a:
            print(t)
            n += 1
        else:
            break


if __name__ == "__main__":
    main()
