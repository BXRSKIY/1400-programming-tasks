def main():
    # 11.60. Дан массив целых чисел. Найти:
    # а) сумму нечётных элементов;
    # б) сумму элементов, кратных заданному числу k;
    # в) сумму элементов массива, кратных a или b.
    #
    # Формат ввода:
    # все числа в одной последовательности:
    # x1 x2 ... xn k a b
    # (последние три числа — k, a, b).
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 4:
        return
    k, a, b = data[-3:]
    arr = data[:-3]
    sum_odd = sum(x for x in arr if x % 2 != 0)
    sum_mult_k = sum(x for x in arr if x % k == 0)
    sum_mult_a_or_b = sum(x for x in arr if (x % a == 0) or (x % b == 0))
    print("a)", sum_odd)
    print("b)", sum_mult_k)
    print("c)", sum_mult_a_or_b)


if __name__ == "__main__":
    main()
