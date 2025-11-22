def main():
    import sys
    # Оценки двух учеников по четырём предметам.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 8:
        raise ValueError("Ожидается 8 оценок (4+4)")
    s1 = sum(data[:4])
    s2 = sum(data[4:8])
    print(s1, s2)


if __name__ == "__main__":
    main()
