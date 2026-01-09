def main():
    # 11.25. Дан массив. Напечатать:
    # а) второй, четвертый и т.д. элементы;
    # б) третий, шестой и т.д. элементы.
    import sys
    arr = sys.stdin.read().split()
    # а) индексы 1,3,5,... (2-й,4-й,...)
    a_part = [arr[i] for i in range(1, len(arr), 2)]
    # б) индексы 2,5,8,... (3-й,6-й,...)
    b_part = [arr[i] for i in range(2, len(arr), 3)]
    print("a)", *a_part)
    print("b)", *b_part)


if __name__ == "__main__":
    main()
