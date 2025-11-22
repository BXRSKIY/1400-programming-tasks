def main():
    import sys
    # Оценки по информатике каждого ученика класса.
    marks = list(map(int, sys.stdin.read().split()))
    count_five = sum(1 for x in marks if x == 5)
    print(count_five)


if __name__ == "__main__":
    main()
