def main():
    import sys
    # Результаты двух спортсменов-пятиборцев в 5 видах спорта.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 чисел (5+5)")
    s1 = sum(data[:5])
    s2 = sum(data[5:10])
    print(s1, s2)


if __name__ == "__main__":
    main()
