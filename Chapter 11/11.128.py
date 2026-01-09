def main():
    # 11.128. Среднедневная температура за каждый день июля.
    # Определить количество самых прохладных дней.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    temps = arr[:31]  # июль — 31 день
    if not temps:
        print(0)
        return
    mn = min(temps)
    cnt = sum(1 for t in temps if t == mn)
    print(cnt)


if __name__ == "__main__":
    main()
