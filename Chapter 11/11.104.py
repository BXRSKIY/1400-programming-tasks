def main():
    # 11.104. Температура каждого дня июля.
    # Найти 7 подряд идущих дней с максимальной суммой температур.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if len(arr) < 7:
        print(1, len(arr))
        return
    best_sum = None
    best_start = 0
    for i in range(0, len(arr) - 6):
        s = sum(arr[i:i+7])
        if best_sum is None or s > best_sum:
            best_sum = s
            best_start = i
    print(best_start + 1, best_start + 7)


if __name__ == "__main__":
    main()
