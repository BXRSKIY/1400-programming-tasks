def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 чисел a1..a10")
    a = data[:10]
    print(sum(a))


if __name__ == "__main__":
    main()
