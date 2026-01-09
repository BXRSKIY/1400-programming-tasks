def main():
    # 11.120. Максимальная скорость каждой из 40 марок авто.
    # Задано V. Найти номера первого и последнего авто со скоростью > V.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    V = data[0]
    speeds = data[1:41]
    first = -1
    last = -1
    for i, s in enumerate(speeds, start=1):
        if s > V:
            if first == -1:
                first = i
            last = i
    print(first, last)


if __name__ == "__main__":
    main()
