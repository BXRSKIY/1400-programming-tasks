def main():
    # 11.137. Дан массив. Определить:
    # а) максимальный элемент и элемент, являющийся максимальным без учёта этого элемента;
    # б) минимальный элемент и элемент, являющийся минимальным без учёта этого элемента;
    # в) номера максимального элемента и «второго по величине максимального»;
    # г) номера минимального элемента и «второго по величине минимального».
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if len(arr) < 2:
        # недостаточно элементов
        return
    # найдём максимальный и второй по величине
    mx = max(arr)
    # исключим одно вхождение mx и найдём следующий максимум
    tmp = arr.copy()
    tmp.remove(mx)
    second_mx = max(tmp)
    mn = min(arr)
    tmp2 = arr.copy()
    tmp2.remove(mn)
    second_mn = min(tmp2)
    # индексы (первое вхождение)
    idx_mx = arr.index(mx) + 1
    idx_second_mx = arr.index(second_mx) + 1
    idx_mn = arr.index(mn) + 1
    idx_second_mn = arr.index(second_mn) + 1
    print("a)", mx, second_mx)
    print("b)", mn, second_mn)
    print("c)", idx_mx, idx_second_mx)
    print("d)", idx_mn, idx_second_mn)


if __name__ == "__main__":
    main()
