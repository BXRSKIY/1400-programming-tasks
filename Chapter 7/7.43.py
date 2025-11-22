def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 целых чисел")
    nums = data[:10]
    s = 0
    for x in nums:
        if x % 10 == 0:
            s += x
    print(s)


if __name__ == "__main__":
    main()
