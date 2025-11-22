def main():
    import sys
    # Числа a1..a8. Проверить, что их произведение меньше 10000.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 8:
        raise ValueError("Ожидается 8 чисел")
    prod = 1.0
    for x in data[:8]:
        prod *= x
    print("YES" if prod < 10000 else "NO")


if __name__ == "__main__":
    main()
