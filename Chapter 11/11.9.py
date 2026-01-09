def main():
    # 11.9. Вывести элементы массива в обратном порядке.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    arr.reverse()
    print(*arr)


if __name__ == "__main__":
    main()
