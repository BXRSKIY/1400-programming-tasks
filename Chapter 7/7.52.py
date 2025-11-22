def main():
    import sys
    # b1..b14
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 14:
        raise ValueError("Ожидается 14 целых чисел b1..b14")
    b = data[:14]
    sum_gt_20 = sum(x for x in b if x > 20)
    sum_lt_50 = sum(x for x in b if x < 50)
    # а) сумма > 100 ?
    cond_a = (sum_gt_20 > 100)
    # б) сумма четная ?
    cond_b = (sum_lt_50 % 2 == 0)
    print("YES" if cond_a else "NO")
    print("YES" if cond_b else "NO")


if __name__ == "__main__":
    main()
