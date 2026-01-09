def main():
    # 11.51. Выяснить, верно ли, что сумма элементов массива
    # есть неотрицательное число.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    s = sum(arr)
    print("YES" if s >= 0 else "NO")


if __name__ == "__main__":
    main()
