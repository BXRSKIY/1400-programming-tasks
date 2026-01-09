def main():
    # 11.161. Удалить из массива, в котором все элементы различны,
    # максимальный и минимальный элементы (оба).
    #
    # Будем удалять оба, по одному, сдвигая и ставя 0 в хвост
    # после каждого удаления.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if len(arr) < 2:
        print(*arr)
        return

    def delete_at(a, idx):
        b = a[:]
        for i in range(idx, len(b)-1):
            b[i] = b[i+1]
        b[-1] = 0
        return b

    # сначала удалим максимум
    mx = max(arr)
    idx_mx = arr.index(mx)
    tmp = delete_at(arr, idx_mx)
    # затем удалим минимум из уже изменённого массива
    mn = min(tmp)
    idx_mn = tmp.index(mn)
    res = delete_at(tmp, idx_mn)
    print(*res)


if __name__ == "__main__":
    main()
