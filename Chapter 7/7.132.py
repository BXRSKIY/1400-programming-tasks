def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 30:
        raise ValueError("Ожидается 30 чисел")
    a = data[:30]
    distinct = 1
    for i in range(1, 30):
        if a[i] != a[i-1]:
            distinct += 1
    print(distinct)


if __name__ == "__main__":
    main()
