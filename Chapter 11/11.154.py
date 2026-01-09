def main():
    # 11.154. Массив из 15 элементов. Переставить в обратном порядке:
    # а) элементы с 3-го по 9-й;
    # б) элементы с (k+1)-го по (s-1)-й, k < s;
    # в) элементы между минимальным и максимальным, включая их.
    #
    # Формат ввода:
    # k s
    # затем 15 элементов массива.
    import sys
    data = sys.stdin.read().split()
    if len(data) < 17:
        return
    k = int(data[0])
    s = int(data[1])
    arr = data[2:2+15]

    # a)
    a_arr = arr[:]
    a_arr[2:9] = reversed(a_arr[2:9])
    print("a)", *a_arr)

    # b)
    b_arr = arr[:]
    k1 = max(1, k)
    s1 = min(len(b_arr), s)
    if k1+1 <= s1-1:
        left = k1
        right = s1-2
        b_arr[k1:s1-1] = reversed(b_arr[k1:s1-1])
    print("b)", *b_arr)

    # c)
    c_arr = arr[:]
    # найдём индексы min и max
    vals = [float(x) for x in c_arr]
    mx = max(vals)
    mn = min(vals)
    i_max = vals.index(mx)
    i_min = vals.index(mn)
    l = min(i_max, i_min)
    r = max(i_max, i_min)
    c_arr[l:r+1] = reversed(c_arr[l:r+1])
    print("c)", *c_arr)


if __name__ == "__main__":
    main()
