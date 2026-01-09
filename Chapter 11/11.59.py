def main():
    # 11.59. Дан массив. Найти сумму элементов массива:
    # а) значение которых не превышает 20;
    # б) больших числа a.
    # Формат ввода: a, затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    a = data[0]
    arr = data[1:]
    sum_le20 = sum(x for x in arr if x <= 20)
    sum_gt_a = sum(x for x in arr if x > a)
    print("a)", sum_le20)
    print("b)", sum_gt_a)


if __name__ == "__main__":
    main()
