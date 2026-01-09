def main():
    # 11.76. В массиве оценки ученика по 10 предметам.
    # Определить общее количество четверок и пятерок.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    grades = arr[:10]
    cnt = sum(1 for g in grades if g == 4 or g == 5)
    print(cnt)


if __name__ == "__main__":
    main()
