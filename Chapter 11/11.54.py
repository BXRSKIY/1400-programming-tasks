def main():
    # 11.54. В массиве — численность книг в разделах библиотеки.
    # Выяснить, верно ли, что общее число книг — шестизначное число.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    total = sum(arr)
    ok = (100000 <= total <= 999999)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
