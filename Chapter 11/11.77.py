def main():
    # 11.77. Определить количество положительных и отрицательных элементов массива.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    print("positive:", pos)
    print("negative:", neg)


if __name__ == "__main__":
    main()
