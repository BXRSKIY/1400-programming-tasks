def main():
    # 11.82. Найти число пар соседних элементов массива,
    # оканчивающихся нулем.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] % 10 == 0 and arr[i+1] % 10 == 0:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
