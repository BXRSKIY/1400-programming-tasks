def main():
    # 11.71. Оценки 25 учеников по химии.
    # Определить количество неуспевающих (оценка < 3).
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    cnt = sum(1 for x in arr if x < 3)
    print(cnt)


if __name__ == "__main__":
    main()
