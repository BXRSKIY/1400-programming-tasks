def main():
    import sys
    # Оценки по алгебре каждого ученика класса.
    marks = list(map(float, sys.stdin.read().split()))
    if not marks:
        raise ValueError("Не введено ни одной оценки")
    print(sum(marks) / len(marks))


if __name__ == "__main__":
    main()
