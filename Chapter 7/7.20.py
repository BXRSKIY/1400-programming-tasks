def main():
    import sys
    # Грузоподъёмность автомобиля C, затем массы всех грузов.
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    C = data[0]
    masses = data[1:]
    total = sum(masses)
    # Верно ли, что общая масса НЕ превысила грузоподъёмность?
    print("YES" if total <= C else "NO")


if __name__ == "__main__":
    main()
