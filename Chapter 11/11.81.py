def main():
    # 11.81. Найти число пар соседних элементов массива,
    # являющихся четными числами.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
