def main():
    import sys
    # Даны числа a1..a10. Найти сумму их квадратов.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 чисел")
    s = sum(x*x for x in data[:10])
    print(s)


if __name__ == "__main__":
    main()
