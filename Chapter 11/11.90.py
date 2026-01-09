def main():
    # 11.90. Найти средние арифметические положительных и отрицательных элементов массива.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    if pos:
        avg_pos = sum(pos) / len(pos)
    else:
        avg_pos = 0.0
    if neg:
        avg_neg = sum(neg) / len(neg)
    else:
        avg_neg = 0.0
    print("positive_avg:", avg_pos)
    print("negative_avg:", avg_neg)


if __name__ == "__main__":
    main()
