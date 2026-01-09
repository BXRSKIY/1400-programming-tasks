def main():
    # 11.52. Дан массив целых чисел. Выяснить, верно ли, что:
    # а) сумма элементов массива есть четное число;
    # б) сумма квадратов элементов массива есть пятизначное число.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    s = sum(arr)
    s2 = sum(x*x for x in arr)
    a_ok = (s % 2 == 0)
    b_ok = (10000 <= s2 <= 99999)
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
