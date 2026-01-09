def main():
    # 11.85. Дан массив. Выяснить, верно ли, что:
    # а) количество элементов, меньших a, равно количеству элементов, больших b;
    # б) количество положительных элементов больше количества отрицательных.
    #
    # Формат ввода: a b затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    a = data[0]
    b = data[1]
    arr = data[2:]
    less_a = sum(1 for x in arr if x < a)
    greater_b = sum(1 for x in arr if x > b)
    a_ok = (less_a == greater_b)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    b_ok = (pos > neg)
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
