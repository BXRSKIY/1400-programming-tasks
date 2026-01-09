def main():
    # 11.39. Дан массив целых чисел.
    # а) все элементы, кратные числу 10, заменить нулем;
    # б) все нечетные элементы удвоить, а четные уменьшить вдвое;
    # в) нечетные элементы уменьшить на m,
    #    а элементы с нечетными номерами увеличить на n.
    #
    # Формат ввода:
    # m n
    # затем элементы массива
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        return
    m = data[0]
    n = data[1]
    arr = data[2:]

    # a)
    arr_a = [0 if x % 10 == 0 else x for x in arr]
    print("a)", *arr_a)

    # b)
    arr_b = [x * 2 if x % 2 != 0 else x // 2 for x in arr]
    print("b)", *arr_b)

    # c)
    arr_c = []
    for i, x in enumerate(arr):
        val = x
        if x % 2 != 0:
            val -= m
        if (i + 1) % 2 == 1:  # нечетный номер
            val += n
        arr_c.append(val)
    print("c)", *arr_c)


if __name__ == "__main__":
    main()
