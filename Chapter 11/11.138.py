def main():
    # 11.138. Максимальная скорость каждой из 40 марок авто.
    # Определить скорости двух самых быстрых автомобилей.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    speeds = arr[:40]
    if len(speeds) < 2:
        print(*speeds)
        return
    mx1 = max(speeds)
    tmp = speeds.copy()
    tmp.remove(mx1)
    mx2 = max(tmp)
    print(mx1, mx2)


if __name__ == "__main__":
    main()
