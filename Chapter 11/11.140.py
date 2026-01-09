def main():
    # 11.140. Результаты 22 спортсменов в беге на 100 м.
    # Определить результаты спортсменов, занявших первое и второе места.
    # Меньшее время — лучше.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    times = arr[:22]
    if len(times) < 2:
        print(*times)
        return
    best1 = min(times)
    tmp = times.copy()
    tmp.remove(best1)
    best2 = min(tmp)
    print(best1, best2)


if __name__ == "__main__":
    main()
