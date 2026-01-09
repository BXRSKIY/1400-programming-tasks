def main():
    # 11.171. Вставить заданное число n в массив целых чисел:
    # а) перед всеми элементами, кратными a;
    # б) после всех отрицательных элементов.
    #
    # Формат ввода:
    # n a
    # затем элементы массива.
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        return
    n = data[0]
    a = data[1]
    arr = data[2:]

    # a) перед всеми кратными a
    a_arr = []
    for x in arr:
        if a != 0 and x % a == 0:
            a_arr.append(n)
        a_arr.append(x)
    print("a)", *a_arr)

    # b) после всех отрицательных
    b_arr = []
    for x in arr:
        b_arr.append(x)
        if x < 0:
            b_arr.append(n)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
