def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 целых чисел")
    xs = data[:12]
    first = xs[0]
    print("YES" if all(x == first for x in xs) else "NO")


if __name__ == "__main__":
    main()
