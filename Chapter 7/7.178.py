def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 целых чисел")
    s = data[:12]
    mx = max(s)
    mn = min(s)
    cnt_max = sum(1 for v in s if v == mx)
    cnt_min = sum(1 for v in s if v == mn)
    print(cnt_max)
    print(cnt_min)


if __name__ == "__main__":
    main()
