def main():
    # 11.61. Определить сумму второго, четвертого, шестого и т. д.
    # элементов массива (элементы с индексами 1,3,5,... в 0-базной нумерации).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    s = sum(arr[1::2])
    print(s)


if __name__ == "__main__":
    main()
