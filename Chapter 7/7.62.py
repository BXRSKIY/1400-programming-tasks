def main():
    import sys
    # Формат: n, p, k, затем n целых чисел a1..an.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        raise ValueError("Ожидаются n, p, k")
    n, p, k = data[0], data[1], data[2]
    if len(data) < 3 + n:
        raise ValueError(f"Ожидается n={n} целых чисел a1..an")
    a = data[3:3+n]
    cnt_gt_p = 0
    cnt_ends_5 = 0
    cnt_mult_k = 0
    for x in a:
        if x > p:
            cnt_gt_p += 1
        if abs(x) % 10 == 5:
            cnt_ends_5 += 1
        if k != 0 and x % k == 0:
            cnt_mult_k += 1
    print(cnt_gt_p)
    print(cnt_ends_5)
    print(cnt_mult_k)


if __name__ == "__main__":
    main()
