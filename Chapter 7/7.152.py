def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 16:
        raise ValueError("Ожидается 15 чисел и n")
    a = data[:15]
    n = data[15]
    best_idx = 0
    best_diff = abs(a[0] - n)
    for i in range(1, 15):
        diff = abs(a[i] - n)
        if diff < best_diff:
            best_diff = diff
            best_idx = i
    print(best_idx + 1, a[best_idx])


if __name__ == "__main__":
    main()
