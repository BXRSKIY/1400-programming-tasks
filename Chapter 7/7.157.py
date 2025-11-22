def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    a = data[1:1+n]
    max_val = a[0]
    min_val = a[0]
    max_pos = 1
    min_pos = 1
    for i in range(2, n+1):
        v = a[i-1]
        if v > max_val or (v == max_val):
            max_val = v
            max_pos = i
        if v < min_val:
            min_val = v
            min_pos = i
    print(max_pos)
    print(min_pos)


if __name__ == "__main__":
    main()
