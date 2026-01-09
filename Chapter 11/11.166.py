def main():
    # 11.166. Вставить в массив:
    # а) число 10 после второго элемента;
    # б) число 100 после m-го элемента.
    #
    # Формат ввода:
    # m
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    m = int(data[0])
    arr = data[1:]

    # a)
    a_arr = arr[:]
    if len(a_arr) >= 2:
        a_arr.insert(2, 10)  # после второго (индекс 1) => вставка на индекс 2
    print("a)", *a_arr)

    # b)
    b_arr = arr[:]
    idx = m  # после m-го => индекс m
    if 0 <= idx <= len(b_arr):
        b_arr.insert(idx, 100.0)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
