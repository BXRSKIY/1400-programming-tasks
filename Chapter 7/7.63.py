def main():
    import sys
    # Оценки по химии каждого ученика класса.
    marks = list(map(int, sys.stdin.read().split()))
    cnt5 = sum(1 for x in marks if x == 5)
    cnt2 = sum(1 for x in marks if x == 2)
    print(cnt5, cnt2)


if __name__ == "__main__":
    main()
