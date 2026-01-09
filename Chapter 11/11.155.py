def main():
    # 11.155. Поменять местами первый отрицательный и последний
    # положительный элементы массива. Возможна ситуация, когда
    # отрицательных или положительных элементов нет.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    first_neg = None
    last_pos = None
    for i, x in enumerate(arr):
        if x < 0 and first_neg is None:
            first_neg = i
        if x > 0:
            last_pos = i
    if first_neg is not None and last_pos is not None:
        arr[first_neg], arr[last_pos] = arr[last_pos], arr[first_neg]
    print(*arr)


if __name__ == "__main__":
    main()
