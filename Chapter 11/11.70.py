def main():
    # 11.70. Осадки за каждый день февраля.
    # Определить количество дней, когда осадков не было.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    cnt = sum(1 for x in arr if x == 0)
    print(cnt)


if __name__ == "__main__":
    main()
