def main():
    # 11.68. Дан массив. Определить количество неотрицательных элементов.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    cnt = sum(1 for x in arr if x >= 0)
    print(cnt)


if __name__ == "__main__":
    main()
