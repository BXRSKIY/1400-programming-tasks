def main():
    # 11.74. Определить количество элементов массива,
    # принадлежащих промежутку от a до b (a и b вводятся с клавиатуры, b > a).
    # Формат ввода: a b затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 2:
        return
    a, b = data[0], data[1]
    arr = data[2:]
    cnt = sum(1 for x in arr if a <= x <= b)
    print(cnt)


if __name__ == "__main__":
    main()
