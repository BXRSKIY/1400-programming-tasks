def main():
    # 11.36. Дан массив вещественных чисел.
    # а) из всех положительных элементов вычесть элемент с номером k1,
    #    из всех отрицательных – число n; нулевые оставить без изменения;
    # б) ко всем нулевым элементам прибавить n,
    #    из всех положительных вычесть a,
    #    к отрицательным прибавить b.
    #
    # Формат ввода:
    # k1 n a b
    # затем элементы массива
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 5:
        return
    k1 = int(data[0])
    n = data[1]
    a = data[2]
    b = data[3]
    arr = data[4:]
    if not arr:
        return

    idx1 = k1 - 1
    v1 = arr[idx1] if 0 <= idx1 < len(arr) else 0.0

    # a)
    a_arr = []
    for x in arr:
        if x > 0:
            a_arr.append(x - v1)
        elif x < 0:
            a_arr.append(x - n)
        else:
            a_arr.append(x)
    print("a)", *a_arr)

    # b)
    b_arr = []
    for x in arr:
        if x == 0:
            b_arr.append(x + n)
        elif x > 0:
            b_arr.append(x - a)
        else:
            b_arr.append(x + b)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
