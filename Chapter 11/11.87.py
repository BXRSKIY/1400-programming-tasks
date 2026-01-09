def main():
    # 11.87. Дан массив. Выяснить, верно ли, что:
    # а) все элементы массива равны между собой;
    # б) все элементы массива попарно различны.
    import sys
    arr = sys.stdin.read().split()
    if not arr:
        print("a) YES")
        print("b) YES")
        return
    a_ok = all(x == arr[0] for x in arr)
    b_ok = (len(set(arr)) == len(arr))
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
