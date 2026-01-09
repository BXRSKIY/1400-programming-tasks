def main():
    # 11.170. Вставить в массив два заданных числа:
    # первое — после любого из максимальных элементов,
    # второе — перед ним.
    # Для определённости возьмём первый по счёту максимальный элемент.
    #
    # Формат ввода:
    # a b
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    a = data[0]
    b = data[1]
    arr = data[2:]
    if not arr:
        print()
        return
    mx = max(arr)
    idx = arr.index(mx)
    # строим новый массив: до max, затем b, потом max, потом a, затем хвост
    res = arr[:idx] + [b, arr[idx], a] + arr[idx+1:]
    print(*res)


if __name__ == "__main__":
    main()
