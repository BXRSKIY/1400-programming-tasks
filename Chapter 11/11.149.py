def main():
    # 11.149. Дан массив. Все его элементы:
    # а) увеличить в 2 раза;
    # б) уменьшить на число A;
    # в) разделить на первый элемент.
    # Формат ввода: A затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    A = data[0]
    arr = data[1:]
    # a)
    a_arr = [x * 2 for x in arr]
    print("a)", *a_arr)
    # b)
    b_arr = [x - A for x in arr]
    print("b)", *b_arr)
    # c)
    if arr and arr[0] != 0:
        c_arr = [x / arr[0] for x in arr]
    else:
        c_arr = ["INF" for _ in arr]
    print("c)", *c_arr)


if __name__ == "__main__":
    main()
