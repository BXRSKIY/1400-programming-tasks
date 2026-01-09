def main():
    # 11.35. Дан массив вещественных чисел.
    # а) ко всем отрицательным элементам прибавить элемент с номером m1,
    #    к остальным – элемент с номером m2;
    # б) все элементы с четными номерами удвоить,
    #    с нечетными – уменьшить на 1.
    #
    # Формат ввода:
    # m1 m2
    # затем элементы массива
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    m1 = int(data[0])
    m2 = int(data[1])
    arr = data[2:]
    if not arr:
        return

    idx1 = m1 - 1
    idx2 = m2 - 1
    v1 = arr[idx1] if 0 <= idx1 < len(arr) else 0.0
    v2 = arr[idx2] if 0 <= idx2 < len(arr) else 0.0

    a_arr = []
    for x in arr:
        if x < 0:
            a_arr.append(x + v1)
        else:
            a_arr.append(x + v2)
    print("a)", *a_arr)

    b_arr = []
    for i, x in enumerate(arr):
        if (i + 1) % 2 == 0:  # четный номер
            b_arr.append(2 * x)
        else:
            b_arr.append(x - 1)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
