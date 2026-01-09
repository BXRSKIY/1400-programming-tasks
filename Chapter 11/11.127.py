def main():
    # 11.127. Стоимость каждой из 60 книг.
    # Определить количество самых дешёвых книг.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    costs = arr[:60]
    if not costs:
        print(0)
        return
    mn = min(costs)
    cnt = sum(1 for x in costs if x == mn)
    print(cnt)


if __name__ == "__main__":
    main()
