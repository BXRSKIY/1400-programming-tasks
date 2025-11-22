def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    x = data[1:1+n]
    if n < 2:
        print(0)
        print(0)
        print(0, 0)
        print(0, 0)
        return
    sums = [x[i] + x[i+1] for i in range(n-1)]
    max_sum = max(sums)
    min_sum = min(sums)
    # первая пара с max_sum
    for i, s in enumerate(sums):
        if s == max_sum:
            first_max_pair = (i+1, i+2)
            break
    # последняя пара с min_sum
    last_min_pair = None
    for i, s in enumerate(sums):
        if s == min_sum:
            last_min_pair = (i+1, i+2)
    print(max_sum)
    print(min_sum)
    print(*first_max_pair)
    print(*last_min_pair)


if __name__ == "__main__":
    main()
