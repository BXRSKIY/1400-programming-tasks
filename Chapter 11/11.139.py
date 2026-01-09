def main():
    # 11.139. Стоимость 30 видов товара.
    # Определить стоимость двух самых дорогих видов.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    costs = arr[:30]
    if len(costs) < 2:
        print(*costs)
        return
    mx1 = max(costs)
    tmp = costs.copy()
    tmp.remove(mx1)
    mx2 = max(tmp)
    print(mx1, mx2)


if __name__ == "__main__":
    main()
