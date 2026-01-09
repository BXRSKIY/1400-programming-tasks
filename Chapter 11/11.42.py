def main():
    # 11.42. Определить:
    # а) сумму всех элементов массива;
    # б) произведение всех элементов массива;
    # в) сумму квадратов всех элементов массива;
    # г) сумму шести первых элементов массива;
    # д) сумму элементов массива с k1-го по k2-й (k2 > k1);
    # е) среднее арифметическое всех элементов массива;
    # ж) среднее арифметическое элементов массива с s1-го по s2-й (s2 > s1).
    #
    # Формат ввода:
    # k1 k2 s1 s2
    # затем элементы массива
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 5:
        return
    k1 = int(data[0])
    k2 = int(data[1])
    s1 = int(data[2])
    s2 = int(data[3])
    arr = data[4:]
    if not arr:
        return

    # a)
    s_all = sum(arr)
    print("a)", s_all)

    # b)
    prod = 1.0
    for x in arr:
        prod *= x
    print("b)", prod)

    # c)
    s_sq = sum(x * x for x in arr)
    print("c)", s_sq)

    # d)
    s_first6 = sum(arr[:6])
    print("d)", s_first6)

    # e)
    i1 = max(1, k1)
    i2 = min(len(arr), k2)
    if i1 <= i2:
        s_k = sum(arr[i1-1:i2])
    else:
        s_k = 0.0
    print("e)", s_k)

    # f)
    avg_all = s_all / len(arr)
    print("f)", avg_all)

    # g)
    j1 = max(1, s1)
    j2 = min(len(arr), s2)
    if j1 <= j2:
        segment = arr[j1-1:j2]
        avg_seg = sum(segment) / len(segment)
    else:
        avg_seg = 0.0
    print("g)", avg_seg)


if __name__ == "__main__":
    main()
