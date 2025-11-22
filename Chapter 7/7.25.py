def main():
    import sys
    # Числа a1..a10. Найти их среднее арифметическое.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 чисел")
    a = data[:10]
    avg = sum(a) / 10.0
    print(avg)


if __name__ == "__main__":
    main()
