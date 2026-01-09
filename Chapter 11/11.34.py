def main():
    # 11.34. Дан массив вещественных чисел.
    # а) из всех положительных элементов вычесть элемент с номером k1,
    #    из остальных – элемент с номером k2;
    # б) элементы с нечетными номерами увеличить на 1,
    #    с четными – уменьшить на 1.
    #
    # Формат ввода:
    # k1 k2
    # затем элементы массива
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    k1 = int(data[0])  # номер с 1
    k2 = int(data[1])  # номер с 1
    arr = data[2:]
    if not arr:
        return

    idx1 = k1 - 1
    idx2 = k2 - 1
    val1 = arr[idx1] if 0 <= idx1 < len(arr) else 0.0
    val2 = arr[idx2] if 0 <= idx2 < len(arr) else 0.0

    # a)
    a_arr = []
    for x in arr:
        if x > 0:
            a_arr.append(x - val1)
        else:
            a_arr.append(x - val2)
    print("a)", *a_arr)

    # b)
    b_arr = []
    for i, x in enumerate(arr):
        if (i + 1) % 2 == 1:  # нечетный номер
            b_arr.append(x + 1)
        else:
            b_arr.append(x - 1)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
