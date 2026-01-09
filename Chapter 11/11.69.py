def main():
    # 11.69. Дан массив целых чисел. Определить:
    # а) количество элементов, отличных от последнего элемента;
    # б) количество элементов, кратных a.
    # Формат ввода: все числа, последнее — a.
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        return
    a = data[-1]
    arr = data[:-1]
    if not arr:
        print("a) 0")
        print("b) 0")
        return
    last = arr[-1]
    cnt_diff_last = sum(1 for x in arr if x != last)
    cnt_mult_a = sum(1 for x in arr if x % a == 0)
    print("a)", cnt_diff_last)
    print("b)", cnt_mult_a)


if __name__ == "__main__":
    main()
