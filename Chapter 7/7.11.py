def main():
    import sys
    # Даны числа a1..a8. Найти их произведение.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 8:
        raise ValueError("Ожидается 8 чисел")
    prod = 1.0
    for x in data[:8]:
        prod *= x
    print(prod)


if __name__ == "__main__":
    main()
