def main():
    # 11.23. Дан массив целых чисел. Напечатать:
    # а) все четные элементы;
    # б) все элементы, оканчивающиеся нулем.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    evens = [x for x in arr if x % 2 == 0]
    end_zero = [x for x in arr if x % 10 == 0]
    print("a)", *evens)
    print("b)", *end_zero)


if __name__ == "__main__":
    main()
