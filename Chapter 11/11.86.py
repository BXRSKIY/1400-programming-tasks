def main():
    # 11.86. Дан массив. Выяснить, верно ли, что:
    # а) массив содержит хотя бы одно положительное и хотя бы одно отрицательное число;
    # б) массив содержит хотя бы одно четное и хотя бы одно нечетное число.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    has_pos = any(x > 0 for x in arr)
    has_neg = any(x < 0 for x in arr)
    a_ok = has_pos and has_neg
    has_even = any(x % 2 == 0 for x in arr)
    has_odd = any(x % 2 != 0 for x in arr)
    b_ok = has_even and has_odd
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
