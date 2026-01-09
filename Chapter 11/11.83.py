def main():
    # 11.83. Найти число элементов массива, которые больше своих
    # соседей (предшествующего и последующего).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    cnt = 0
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
