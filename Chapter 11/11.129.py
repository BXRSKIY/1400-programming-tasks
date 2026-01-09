def main():
    # 11.129. Дан массив. Найти номера всех элементов:
    # а) с минимальным значением;
    # б) с максимальным значением.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        print("a)")
        print("b)")
        return
    mn = min(arr)
    mx = max(arr)
    # номера считаем с 1
    idx_min = [i+1 for i,x in enumerate(arr) if x == mn]
    idx_max = [i+1 for i,x in enumerate(arr) if x == mx]
    print("a)", *idx_min)
    print("b)", *idx_max)


if __name__ == "__main__":
    main()
