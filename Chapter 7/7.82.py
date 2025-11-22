def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} целых чисел")
    a = data[1:1+n]
    cnt_equal = cnt_zero_pairs = cnt_even_pairs = cnt_end5_pairs = 0
    for i in range(n-1):
        x, y = a[i], a[i+1]
        if x == y:
            cnt_equal += 1
        if x == 0 and y == 0:
            cnt_zero_pairs += 1
        if x % 2 == 0 and y % 2 == 0:
            cnt_even_pairs += 1
        if abs(x) % 10 == 5 and abs(y) % 10 == 5:
            cnt_end5_pairs += 1
    print(cnt_equal)
    print(cnt_zero_pairs)
    print(cnt_even_pairs)
    print(cnt_end5_pairs)


if __name__ == "__main__":
    main()
