def main():
    import sys
    # Сопротивления элементов, соединённых последовательно.
    resistances = list(map(float, sys.stdin.read().split()))
    print(sum(resistances))


if __name__ == "__main__":
    main()
