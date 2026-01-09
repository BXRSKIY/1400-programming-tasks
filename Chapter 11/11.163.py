def main():
    # 11.163. Удалить из массива:
    # а) все отрицательные элементы;
    # б) все элементы, большие n;
    # в) все элементы с n1-го по n2-й (n1 <= n2).
    #
    # Удаление — каждый раз смещение влево и 0 в хвост.
    #
    # Формат ввода:
    # n n1 n2
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 4:
        return
    n = data[0]
    n1 = int(data[1])
    n2 = int(data[2])
    arr = data[3:]

    def delete_at(a, pos):
        b = a[:]
        if 0 <= pos < len(b):
            for i in range(pos, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0.0
        return b

    # a) удалить все отрицательные
    a_arr = arr[:]
    i = 0
    while i < len(a_arr):
        if a_arr[i] < 0:
            a_arr = delete_at(a_arr, i)
        else:
            i += 1
    print("a)", *a_arr)

    # b) удалить все > n
    b_arr = arr[:]
    i = 0
    while i < len(b_arr):
        if b_arr[i] > n:
            b_arr = delete_at(b_arr, i)
        else:
            i += 1
    print("b)", *b_arr)

    # c) удалить элементы с n1 по n2
    c_arr = arr[:]
    # n1, n2 — 1-базные
    if n1 <= n2:
        count = max(0, min(len(c_arr), n2) - max(1, n1) + 1)
        for _ in range(count):
            # каждый раз удаляем элемент с индексом n1-1
            c_arr = delete_at(c_arr, n1-1)
    print("c)", *c_arr)


if __name__ == "__main__":
    main()
