def main():
    # 11.143. Среднедневная температура за каждый день июля.
    # Определить даты двух самых тёплых дней.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    temps = arr[:31]
    if len(temps) < 2:
        # выведем все имеющиеся дни
        print(*range(1, len(temps)+1))
        return
    mx1 = max(temps)
    idx1 = temps.index(mx1)
    tmp = temps.copy()
    tmp.pop(idx1)
    mx2 = max(tmp)
    # найти индекс второго максимума в исходном списке (первое вхождение)
    idx2 = temps.index(mx2)
    print(idx1+1, idx2+1)


if __name__ == "__main__":
    main()
