def main():
    import sys
    # Оценки по физике 20 учеников класса.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 оценок")
    marks = data[:20]
    print(sum(marks) / 20.0)


if __name__ == "__main__":
    main()
