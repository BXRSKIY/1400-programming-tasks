def main():
    # 11.27. Дан массив целых чисел. Вывести на экран
    # сначала его четные элементы, затем нечетные.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    print("even:", *evens)
    print("odd:", *odds)


if __name__ == "__main__":
    main()
