def main():
    import sys
    # Оценки по физике каждого ученика двух классов, численность одинакова.
    marks = list(map(float, sys.stdin.read().split()))
    if not marks or len(marks) % 2 != 0:
        raise ValueError("Должно быть четное количество оценок")
    n = len(marks) // 2
    class1 = marks[:n]
    class2 = marks[n:]
    avg1 = sum(class1) / n
    avg2 = sum(class2) / n
    print(avg1, avg2)


if __name__ == "__main__":
    main()
