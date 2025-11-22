def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + 2*n:
        raise ValueError(f"Ожидается {n} пар чисел")
    vals = data[1:1+2*n]
    max_sum = None
    min_prod = None
    for i in range(0, len(vals), 2):
        a = vals[i]
        b = vals[i+1]
        s = a + b
        p = a * b
        if max_sum is None or s > max_sum:
            max_sum = s
        if min_prod is None or p < min_prod:
            min_prod = p
    print(max_sum)
    print(min_prod)


if __name__ == "__main__":
    main()
