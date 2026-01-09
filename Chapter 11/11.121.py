def main():
    # 11.121. Осадки за каждый день июля.
    # Найти дату самого дождливого дня: первый и последний, если несколько.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:31]
    if not days:
        print(-1, -1)
        return
    mx = max(days)
    first = last = None
    for i, x in enumerate(days, start=1):
        if x == mx:
            if first is None:
                first = i
            last = i
    print(first, last)


if __name__ == "__main__":
    main()
