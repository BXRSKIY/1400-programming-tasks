def main():
    # 11.26. Дан массив. Вывести на экран
    # сначала его неотрицательные элементы, затем отрицательные.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    nonneg = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    print("nonneg:", *nonneg)
    print("neg:", *neg)


if __name__ == "__main__":
    main()
