def main():
    # 11.158. Удалить из массива, в котором все элементы различны:
    # а) максимальный элемент;
    # б) минимальный элемент.
    #
    # Удаление — смещение последующих влево и 0 в конец.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        return

    def delete_at(a, idx):
        b = a[:]
        for i in range(idx, len(b)-1):
            b[i] = b[i+1]
        b[-1] = 0
        return b

    # a) удалить максимум
    mx = max(arr)
    idx_max = arr.index(mx)
    a_arr = delete_at(arr, idx_max)
    print("a)", *a_arr)

    # b) удалить минимум
    mn = min(arr)
    idx_min = arr.index(mn)
    b_arr = delete_at(arr, idx_min)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
