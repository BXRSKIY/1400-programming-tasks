def main():
    # 11.172. Вставить в массив два числа:
    # первое со значением n — перед всеми элементами, большими n,
    # второе со значением m — после всех элементов, меньших m.
    #
    # Формат ввода:
    # n m
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    n = data[0]
    m = data[1]
    arr = data[2:]

    res = []
    for x in arr:
        # перед всеми > n
        if x > n:
            res.append(n)
        res.append(x)
        # после всех < m
        if x < m:
            res.append(m)
    print(*res)


if __name__ == "__main__":
    main()
