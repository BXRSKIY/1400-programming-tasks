def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 чисел")
    x = data[:15]
    for i in range(1, 15):
        if x[i] < x[i-1]:
            print("NO", i+1)
            return
    print("YES")


if __name__ == "__main__":
    main()
