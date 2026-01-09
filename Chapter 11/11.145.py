def main():
    # 11.145. Среднедневная температура за каждый день февраля.
    # Определить даты двух самых холодных дней.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    temps = arr[:29]  # пусть февраль 29 дней, но можно взять все
    if len(temps) < 2:
        print(*range(1, len(temps)+1))
        return
    mn1 = min(temps)
    idx1 = temps.index(mn1)
    tmp = temps.copy()
    tmp.pop(idx1)
    mn2 = min(tmp)
    idx2 = temps.index(mn2)
    print(idx1+1, idx2+1)


if __name__ == "__main__":
    main()
