def main():
    # 11.102. Элемент, наиболее близкий к среднему значению.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        return
    avg = sum(arr) / len(arr)
    best = arr[0]
    best_diff = abs(arr[0] - avg)
    for x in arr[1:]:
        d = abs(x - avg)
        if d < best_diff:
            best_diff = d
            best = x
    print(best)


if __name__ == "__main__":
    main()
