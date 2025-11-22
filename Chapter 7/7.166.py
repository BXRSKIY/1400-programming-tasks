def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 40:
        raise ValueError("Ожидается 20 пар (U, R)")
    min_current = None
    idx_min = 0
    for i in range(20):
        u = data[2*i]
        r = data[2*i+1]
        if r == 0:
            continue
        I = u / r
        if min_current is None or I < min_current:
            min_current = I
            idx_min = i + 1
    print(idx_min)


if __name__ == "__main__":
    main()
