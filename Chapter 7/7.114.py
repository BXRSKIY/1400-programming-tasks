def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 14:
        raise ValueError("Ожидается 14 целых чисел d1..d14")
    d = data[:14]
    evens = [x for x in d if x % 2 == 0]
    if not evens:
        print(0.0)
    else:
        print(sum(evens) / len(evens))


if __name__ == "__main__":
    main()
