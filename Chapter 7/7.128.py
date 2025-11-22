def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 натуральных чисел")
    b = data[:12]
    for i, v in enumerate(b, start=1):
        if v % 10 == 7:
            print("YES", i)
            return
    print("NO", 0)


if __name__ == "__main__":
    main()
