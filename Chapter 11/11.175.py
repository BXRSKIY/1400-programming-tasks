def main():
    # 11.175*. Вставить число n между всеми соседними элементами,
    # имеющими одинаковый знак.
    #
    # Формат ввода:
    # n
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[1:]
    if not arr:
        print()
        return
    res = [arr[0]]
    for i in range(1, len(arr)):
        prev = arr[i-1]
        cur = arr[i]
        # одинаковый знак: произведение > 0
        if prev * cur > 0:
            res.append(n)
        res.append(cur)
    print(*res)


if __name__ == "__main__":
    main()
