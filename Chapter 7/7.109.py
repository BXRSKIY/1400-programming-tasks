def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 целых чисел")
    xs = data[:12]
    evens = [x for x in xs if x % 2 == 0]
    odds = [x for x in xs if x % 2 != 0]
    avg_even = sum(evens) / len(evens) if evens else 0.0
    avg_odd  = sum(odds) / len(odds) if odds else 0.0
    print(avg_even, avg_odd)


if __name__ == "__main__":
    main()
