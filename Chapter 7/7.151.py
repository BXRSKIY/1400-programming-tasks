def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        print(0)
        return
    m = data[0]
    if len(data) < 1 + m:
        raise ValueError(f"Ожидается m={m} чисел 0/1")
    xs = data[1:1+m]
    min_len = None
    cur = 0
    for x in xs:
        if x == 0:
            cur += 1
        else:
            if cur > 0:
                if min_len is None or cur < min_len:
                    min_len = cur
                cur = 0
    if cur > 0:
        if min_len is None or cur < min_len:
            min_len = cur
    print(min_len if min_len is not None else 0)


if __name__ == "__main__":
    main()
