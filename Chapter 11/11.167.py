def main():
    # 11.167. Вставить заданное число в массив целых чисел:
    # а) после первого отрицательного элемента;
    # б) перед последним чётным элементом.
    #
    # Формат ввода:
    # n
    # затем элементы массива.
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[1:]

    # a) после первого отрицательного
    a_arr = arr[:]
    pos = None
    for i, x in enumerate(a_arr):
        if x < 0:
            pos = i
            break
    if pos is None:
        # если нет отрицательных — добавим в конец
        a_arr.append(n)
    else:
        a_arr.insert(pos+1, n)
    print("a)", *a_arr)

    # b) перед последним чётным
    b_arr = arr[:]
    pos_even = None
    for i in range(len(b_arr)-1, -1, -1):
        if b_arr[i] % 2 == 0:
            pos_even = i
            break
    if pos_even is None:
        b_arr.insert(0, n)
    else:
        b_arr.insert(pos_even, n)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
