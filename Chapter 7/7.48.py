def main():
    import sys
    # Количество страниц в газетах и журналах.
    # Известно: газета <= 16 страниц, любой журнал имеет больше страниц,
    # чем любая газета. Найти общее число страниц во всех журналах.
    pages = list(map(int, sys.stdin.read().split()))
    total_mag_pages = 0
    for p in pages:
        if p > 16:
            total_mag_pages += p
    print(total_mag_pages)


if __name__ == "__main__":
    main()
