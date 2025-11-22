def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 натуральных чисел")
    a = data[:15]
    for i in range(14):
        if a[i] == a[i+1]:
            print(i+1, i+2)
            return
    print(0, 0)


if __name__ == "__main__":
    main()
