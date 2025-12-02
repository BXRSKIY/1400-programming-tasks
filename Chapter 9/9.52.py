from math import gcd

def main():
    # Даны целые числа p и q. Получить все делители числа q,
    # взаимно простые с p.
    p, q = map(int, input().split())
    res = []
    for d in range(1, abs(q) + 1):
        if q % d == 0 and gcd(d, p) == 1:
            res.append(d)
    print(*res)


if __name__ == "__main__":
    main()
