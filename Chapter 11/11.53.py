def main():
    # 11.53. В массиве — численность учеников в каждом классе.
    # Выяснить, верно ли, что общее число учеников — четырёхзначное.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    total = sum(arr)
    ok = (1000 <= total <= 9999)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
