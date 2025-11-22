def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 целых чисел")
    a = data[:10]
    pos_count = sum(1 for x in a if x > 0)
    print("YES" if pos_count <= 5 else "NO")


if __name__ == "__main__":
    main()
