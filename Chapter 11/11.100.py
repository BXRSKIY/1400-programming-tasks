def main():
    # 11.100. В массиве оценки по информатике 22 учеников.
    # Определить количество учеников, оценка которых меньше средней,
    # и вывести номера элементов массива, соответствующих таким ученикам.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    grades = arr[:22]
    if not grades:
        print(0)
        return
    avg = sum(grades) / len(grades)
    idxs = [i+1 for i, g in enumerate(grades) if g < avg]
    print(len(idxs))
    print(*idxs)


if __name__ == "__main__":
    main()
