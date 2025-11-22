def main():
    import sys
    # Оценки по 10 предметам.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 оценок")
    marks = data[:10]
    print(sum(marks) / 10.0)


if __name__ == "__main__":
    main()
