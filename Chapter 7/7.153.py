def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 14:
        raise ValueError("Ожидается 14 целых чисел")
    xs = data[:14]
    max_even = None
    for x in xs:
        if x % 2 == 0:
            if max_even is None or x > max_even:
                max_even = x
    print(max_even if max_even is not None else 0)


if __name__ == "__main__":
    main()
