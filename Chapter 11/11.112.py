def main():
    # 11.112. Дан массив. Найти:
    # а) max; б) min; в) max-min;
    # г) индекс max; д) индексы min и max.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        return
    mx = max(arr)
    mn = min(arr)
    diff = mx - mn
    idx_max = arr.index(mx) + 1
    idx_min = arr.index(mn) + 1
    print("a)", mx)
    print("b)", mn)
    print("c)", diff)
    print("d)", idx_max)
    print("e)", idx_min, idx_max)


if __name__ == "__main__":
    main()
