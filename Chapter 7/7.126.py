def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 чисел a1..a15")
    a = data[:15]
    for i, v in enumerate(a, start=1):
        if v < 0:
            print("YES", i)
            return
    print("NO", 0)


if __name__ == "__main__":
    main()
