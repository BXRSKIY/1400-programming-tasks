def main():
    import sys
    # Целые числа a1..a9. Проверить, что их сумма чётная.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 9:
        raise ValueError("Ожидается 9 целых чисел")
    s = sum(data[:9])
    print("YES" if s % 2 == 0 else "NO")


if __name__ == "__main__":
    main()
