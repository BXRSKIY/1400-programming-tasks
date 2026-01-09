def main():
    # 11.103. В массиве из 20 элементов найти пять соседних
    # элементов с максимальной суммой.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if len(arr) < 5:
        print(*arr)
        return
    best_sum = None
    best_i = 0
    for i in range(0, len(arr) - 4):
        s = sum(arr[i:i+5])
        if best_sum is None or s > best_sum:
            best_sum = s
            best_i = i
    print(*arr[best_i:best_i+5])


if __name__ == "__main__":
    main()
