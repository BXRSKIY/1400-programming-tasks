def main():
    # 11.126. Осадки за каждый день октября.
    # Определить количество дней, когда выпало самое большое число осадков.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    # октябрь — 31 день, но в условии явно не указано, используем все введённые
    if not arr:
        print(0)
        return
    mx = max(arr)
    cnt = sum(1 for x in arr if x == mx)
    print(cnt)


if __name__ == "__main__":
    main()
