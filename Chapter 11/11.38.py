def main():
    # 11.38. Дан массив целых чисел.
    # а) все элементы, оканчивающиеся цифрой 4, уменьшить вдвое;
    # б) все четные элементы заменить на их квадраты,
    #    а нечетные удвоить;
    # в) четные элементы увеличить на a,
    #    а из элементов с четными номерами вычесть b.
    #
    # Формат ввода:
    # a b
    # затем элементы массива
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        return
    a = data[0]
    b = data[1]
    arr = data[2:]

    # a)
    arr_a = [x // 2 if x % 10 == 4 or x % 10 == -6 else x for x in arr]
    # Используем x%10==4, а для отрицательных -6 (например, -14 % 10 == 6)
    print("a)", *arr_a)

    # b)
    arr_b = [x * x if x % 2 == 0 else 2 * x for x in arr]
    print("b)", *arr_b)

    # c)
    arr_c = []
    for i, x in enumerate(arr):
        val = x
        if x % 2 == 0:
            val += a
        if (i + 1) % 2 == 0:  # четный номер
            val -= b
        arr_c.append(val)
    print("c)", *arr_c)


if __name__ == "__main__":
    main()
