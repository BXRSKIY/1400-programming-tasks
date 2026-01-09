def main():
    # 11.150. Дан массив. Все его элементы:
    # а) уменьшить на 20;
    # б) умножить на последний элемент;
    # в) увеличить на число B.
    # Формат ввода: B затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    B = data[0]
    arr = data[1:]
    # a)
    a_arr = [x - 20 for x in arr]
    print("a)", *a_arr)
    # b)
    if arr:
        last = arr[-1]
        b_arr = [x * last for x in arr]
    else:
        b_arr = []
    print("b)", *b_arr)
    # c)
    c_arr = [x + B for x in arr]
    print("c)", *c_arr)


if __name__ == "__main__":
    main()
