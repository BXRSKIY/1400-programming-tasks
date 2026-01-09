def main():
    # 11.80. Оценки по иностранному языку 22 учеников.
    # Определить количество 5,4,3,2.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    grades = arr[:22]
    c5 = sum(1 for x in grades if x == 5)
    c4 = sum(1 for x in grades if x == 4)
    c3 = sum(1 for x in grades if x == 3)
    c2 = sum(1 for x in grades if x == 2)
    print("5:", c5)
    print("4:", c4)
    print("3:", c3)
    print("2:", c2)


if __name__ == "__main__":
    main()
