def main():
    import sys
    # Формат: n, x, затем n целых a1..an
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются n и x")
    n = data[0]
    x = data[1]
    if len(data) < 2 + n:
        raise ValueError(f"Ожидается n={n} целых чисел")
    a = data[2:2+n]
    neg_cnt = sum(1 for v in a if v < 0)
    print("YES" if neg_cnt > x else "NO")


if __name__ == "__main__":
    main()
