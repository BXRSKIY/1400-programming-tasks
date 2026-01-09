def main():
    # 11.37. Дан массив вещественных чисел.
    # а) ко всем отрицательным элементам прибавить элемент с номером a1,
    #    из всех нулевых вычесть число b; положительные оставить без изменения;
    # б) из всех положительных элементов вычесть a,
    #    из всех отрицательных вычесть b,
    #    ко всем нулевым элементам прибавить c.
    #
    # Формат ввода:
    # a1 b a b2 c
    # (чтобы не путаться в буквах задачи, назовём второе b как b2)
    # затем элементы массива
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 6:
        return
    a1 = int(data[0])
    b = data[1]
    a = data[2]
    b2 = data[3]
    c = data[4]
    arr = data[5:]
    if not arr:
        return

    idx = a1 - 1
    v = arr[idx] if 0 <= idx < len(arr) else 0.0

    # a)
    a_arr = []
    for x in arr:
        if x < 0:
            a_arr.append(x + v)
        elif x == 0:
            a_arr.append(x - b)
        else:
            a_arr.append(x)
    print("a)", *a_arr)

    # b)
    b_arr = []
    for x in arr:
        if x > 0:
            b_arr.append(x - a)
        elif x < 0:
            b_arr.append(x - b2)
        else:
            b_arr.append(x + c)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
