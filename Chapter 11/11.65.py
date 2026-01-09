def main():
    # 11.65. Дан массив целых чисел. Выяснить, верно ли, что:
    # а) сумма элементов, которые больше 20, превышает 100;
    # б) сумма элементов, которые меньше 50, есть чётное число.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    sum_gt20 = sum(x for x in arr if x > 20)
    sum_lt50 = sum(x for x in arr if x < 50)
    a_ok = (sum_gt20 > 100)
    b_ok = (sum_lt50 % 2 == 0)
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
