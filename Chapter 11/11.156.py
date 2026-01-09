def main():
    # 11.156. Удалить из массива:
    # а) третий элемент;
    # б) k-й элемент.
    #
    # Под удалением понимается:
    #  1) смещение всех последующих элементов влево на 1;
    #  2) присваивание последнему элементу значения 0.
    #
    # Формат ввода:
    # k
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 2:
        return
    k = int(data[0])
    arr = data[1:]

    def delete_at(a, idx):
        b = a[:]
        if 0 <= idx < len(b):
            for i in range(idx, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0
        return b

    a_arr = delete_at(arr, 2)      # третий элемент (индекс 2)
    print("a)", *a_arr)
    b_arr = delete_at(arr, k-1)    # k-й элемент
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
