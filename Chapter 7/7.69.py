def main():
    import sys
    # Оценки по информатике 20 учеников.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 оценок")
    marks = data[:20]
    count = sum(1 for x in marks if x == 5)
    print(count)


if __name__ == "__main__":
    main()
