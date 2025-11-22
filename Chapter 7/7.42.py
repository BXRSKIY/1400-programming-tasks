def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 целых чисел d1..d10")
    ds = data[:10]
    s = 0
    for x in ds:
        if x % 2 == 0:
            s += x
    print(s)


if __name__ == "__main__":
    main()
