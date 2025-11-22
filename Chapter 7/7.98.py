def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 натуральных чисел")
    d = data[:20]
    for i in range(19):
        if d[i] == d[i+1]:
            print(i+1, i+2)
            return
    print(0, 0)


if __name__ == "__main__":
    main()
