def main():
    # 11.160. Удалить из массива:
    # а) первый отрицательный элемент (если есть);
    # б) последний чётный элемент (если есть).
    #
    # Удаление — смещение влево и 0 в конец.
    import sys
    arr = list(map(int, sys.stdin.read().split()))

    def delete_at(a, idx):
        b = a[:]
        if 0 <= idx < len(b):
            for i in range(idx, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0
        return b

    # a)
    idx_neg = None
    for i, x in enumerate(arr):
        if x < 0:
            idx_neg = i
            break
    if idx_neg is not None:
        a_arr = delete_at(arr, idx_neg)
    else:
        a_arr = arr[:]
    print("a)", *a_arr)

    # b)
    idx_even = None
    for i in range(len(arr)-1, -1, -1):
        if arr[i] % 2 == 0:
            idx_even = i
            break
    if idx_even is not None:
        b_arr = delete_at(arr, idx_even)
    else:
        b_arr = arr[:]
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
