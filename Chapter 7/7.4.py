def main():
    import sys
    # Массы всех предметов (количество не задано явно).
    # Считаем, что на входе только массы, которые нужно суммировать.
    masses = list(map(float, sys.stdin.read().split()))
    print(sum(masses))


if __name__ == "__main__":
    main()
