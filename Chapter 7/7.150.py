def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        print(0)
        return
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    d = data[1:1+n]
    max_len = 0
    cur = 0
    for x in d:
        if x % 2 == 0:
            cur += 1
            if cur > max_len:
                max_len = cur
        else:
            cur = 0
    print(max_len)


if __name__ == "__main__":
    main()
