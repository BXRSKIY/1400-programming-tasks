def main():
    # 11.55. В массиве — массы 30 предметов, загружаемых в грузовик.
    # Грузоподъёмность автомобиля задаётся первым числом входных данных.
    # Определить, не превышает ли общая масса всех предметов грузоподъёмность.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    capacity = data[0]
    masses = data[1:31]
    total = sum(masses)
    print("YES" if total <= capacity else "NO")


if __name__ == "__main__":
    main()
