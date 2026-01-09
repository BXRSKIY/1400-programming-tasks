def main():
    # 11.124. Для массива найти количество максимумов и минимумов.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        print("a) 0")
        print("b) 0")
        return
    mx = max(arr)
    mn = min(arr)
    cmax = sum(1 for x in arr if x == mx)
    cmin = sum(1 for x in arr if x == mn)
    print("a)", cmax)
    print("b)", cmin)


if __name__ == "__main__":
    main()
