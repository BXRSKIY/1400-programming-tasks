def main():
    # 11.84. Дан массив вещественных чисел. Выяснить, верно ли, что:
    # а) количество положительных элементов равно количеству отрицательных;
    # б) модуль максимального элемента массива убывает при просмотре массива слева направо.
    # (Интерпретация б): последовательность модулей элементов строго убывает.)
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    a_ok = (pos == neg)

    b_ok = True
    if arr:
        prev = abs(arr[0])
        for x in arr[1:]:
            cur = abs(x)
            if cur >= prev:
                b_ok = False
                break
            prev = cur
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
