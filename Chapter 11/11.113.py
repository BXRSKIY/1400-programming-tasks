def main():
    # 11.113. Количество страниц в каждой из 100 книг.
    # Найти число страниц в самой толстой книге.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    books = arr[:100]
    if not books:
        print(0)
    else:
        print(max(books))


if __name__ == "__main__":
    main()
