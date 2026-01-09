def main():
    # 11.151. Дан массив. Поменять местами:
    # а) второй и пятый элементы;
    # б) m-й и n-й элементы;
    # в) третий и максимальный элементы (если максимумов несколько — первый);
    # г) первый и минимальный элементы (если минимумов несколько — последний).
    #
    # Формат ввода:
    # m n
    # затем элементы массива (не менее 5).
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    m = int(data[0])
    n = int(data[1])
    arr = data[2:]

    def swap_copy(a, i, j):
        b = a[:]
        if 0 <= i < len(b) and 0 <= j < len(b):
            b[i], b[j] = b[j], b[i]
        return b

    # a)
    a_arr = swap_copy(arr, 1, 4)  # 2-й и 5-й (0-базные 1 и 4)
    print("a)", *a_arr)

    # b)
    b_arr = swap_copy(arr, m-1, n-1)
    print("b)", *b_arr)

    # c)
    if arr:
        mx = max(arr)
        idx_max = arr.index(mx)  # первое вхождение
        c_arr = swap_copy(arr, 2, idx_max)  # 3-й и max
    else:
        c_arr = arr
    print("c)", *c_arr)

    # d)
    if arr:
        mn = min(arr)
        # последнее вхождение минимума
        idx_min = len(arr) - 1 - arr[::-1].index(mn)
        d_arr = swap_copy(arr, 0, idx_min)
    else:
        d_arr = arr
    print("d)", *d_arr)


if __name__ == "__main__":
    main()
