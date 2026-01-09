def main():
    # 11.89. Даны массивы X и Y одинаковой длины.
    # Найти среднее арифметическое соответствующих элементов массивов.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    # будем считать, что длина массивов одинаковая и делится пополам
    n = len(data) // 2
    X = data[:n]
    Y = data[n:n*2]
    res = []
    for x, y in zip(X, Y):
        res.append((x + y) / 2.0)
    print(*res)


if __name__ == "__main__":
    main()
