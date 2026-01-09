def main():
    # 11.174. Вставить число a в массив целых чисел
    # после всех элементов, в которых есть цифра 5.
    #
    # Формат ввода:
    # a
    # затем элементы массива.
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    a = int(data[0])
    arr = list(map(int, data[1:]))

    def has_digit5(x: int) -> bool:
        x = abs(x)
        if x == 0:
            return False
        while x > 0:
            if x % 10 == 5:
                return True
            x //= 10
        return False

    res = []
    for x in arr:
        res.append(x)
        if has_digit5(x):
            res.append(a)
    print(*res)


if __name__ == "__main__":
    main()
