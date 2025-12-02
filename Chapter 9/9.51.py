from math import gcd

def main():
    # Даны целые числа n и m. Получить все натуральные числа,
    # меньшие n и взаимно простые с m.
    n, m = map(int, input().split())
    res = []
    for k in range(1, n):
        if gcd(k, m) == 1:
            res.append(k)
    print(*res)


if __name__ == "__main__":
    main()
