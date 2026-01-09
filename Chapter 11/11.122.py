def main():
    # 11.122. Стоимость 1 кг 30 видов конфет.
    # Найти первый и последний самый дешёвый вид.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    costs = arr[:30]
    if not costs:
        print(-1, -1)
        return
    mn = min(costs)
    first = last = None
    for i, x in enumerate(costs, start=1):
        if x == mn:
            if first is None:
                first = i
            last = i
    print(first, last)


if __name__ == "__main__":
    main()
