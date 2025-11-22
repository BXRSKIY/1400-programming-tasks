def main():
    import sys
    # Оценки по физике каждого ученика класса.
    marks = list(map(int, sys.stdin.read().split()))
    c2 = c3 = c4 = c5 = 0
    for m in marks:
        if m == 2:
            c2 += 1
        elif m == 3:
            c3 += 1
        elif m == 4:
            c4 += 1
        elif m == 5:
            c5 += 1
    print(c5, c4, c3, c2)


if __name__ == "__main__":
    main()
