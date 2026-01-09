def main():
    # 11.41. Дан массив целых чисел. Выяснить:
    # а) является ли s-й элемент массива положительным числом;
    # б) является ли k-й элемент массива четным числом;
    # в) какой элемент массива больше: k-й или s-й.
    #
    # Формат ввода:
    # s k
    # затем элементы массива
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        return
    s = int(data[0])
    k = int(data[1])
    arr = data[2:]
    idx_s = s - 1
    idx_k = k - 1
    if 0 <= idx_s < len(arr):
        print("a)", "YES" if arr[idx_s] > 0 else "NO")
    else:
        print("a) index out of range")
    if 0 <= idx_k < len(arr):
        print("b)", "YES" if arr[idx_k] % 2 == 0 else "NO")
    else:
        print("b) index out of range")
    if 0 <= idx_s < len(arr) and 0 <= idx_k < len(arr):
        if arr[idx_k] > arr[idx_s]:
            print("c) k")
        elif arr[idx_s] > arr[idx_k]:
            print("c) s")
        else:
            print("c) equal")
    else:
        print("c) index out of range")


if __name__ == "__main__":
    main()
