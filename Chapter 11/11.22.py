def main():
    # 11.22. Дан массив. Напечатать:
    # а) все неотрицательные элементы;
    # б) все элементы, не превышающие число 100.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    nonneg = [x for x in arr if x >= 0]
    le100 = [x for x in arr if x <= 100]
    print("a)", *nonneg)
    print("b)", *le100)


if __name__ == "__main__":
    main()
