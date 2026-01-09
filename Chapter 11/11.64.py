def main():
    # 11.64. Определить частное от деления суммы положительных
    # элементов массива на модуль суммы отрицательных элементов.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    sum_pos = sum(x for x in arr if x > 0)
    sum_neg = sum(x for x in arr if x < 0)
    if sum_neg == 0:
        print("INF")  # деление на ноль — частное не определено
    else:
        q = sum_pos / abs(sum_neg)
        print(q)


if __name__ == "__main__":
    main()
