def main():
    # 11.164. Дан массив целых чисел. Удалить из него:
    # а) все чётные элементы, стоящие на нечётных местах;
    # б) все элементы, кратные 3 или 5.
    #
    # Удаление — смещение влево и 0 в хвост.
    import sys
    arr = list(map(int, sys.stdin.read().split()))

    def delete_at(a, pos):
        b = a[:]
        if 0 <= pos < len(b):
            for i in range(pos, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0
        return b

    # a) четные на нечетных местах (места считаем с 1)
    a_arr = arr[:]
    i = 0
    while i < len(a_arr):
        pos = i + 1
        if pos % 2 == 1 and a_arr[i] % 2 == 0:
            a_arr = delete_at(a_arr, i)
        else:
            i += 1
    print("a)", *a_arr)

    # b) кратные 3 или 5
    b_arr = arr[:]
    i = 0
    while i < len(b_arr):
        if b_arr[i] % 3 == 0 or b_arr[i] % 5 == 0:
            b_arr = delete_at(b_arr, i)
        else:
            i += 1
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
