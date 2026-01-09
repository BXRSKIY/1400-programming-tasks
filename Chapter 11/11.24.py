def main():
    # 11.24. Дан массив натуральных чисел. Напечатать все элементы,
    # являющиеся:
    # а) двузначными числами;
    # б) трехзначными числами.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    two_digit = [x for x in arr if 10 <= x <= 99]
    three_digit = [x for x in arr if 100 <= x <= 999]
    print("a)", *two_digit)
    print("b)", *three_digit)


if __name__ == "__main__":
    main()
