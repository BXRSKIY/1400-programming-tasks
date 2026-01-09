def main():
    # 11.146. В массиве a записаны результаты 23 спортсменов
    # в беге на 100 м (в сотых долях секунды).
    # Составить команду из 4 спортсменов с минимальной суммой результатов.
    # То есть нужно выбрать 4 наименьших значения.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    times = arr[:23]
    if len(times) < 4:
        print(*times)
        return
    # возьмём 4 наименьших результата
    sorted_times = sorted(times)
    team = sorted_times[:4]
    print(*team)


if __name__ == "__main__":
    main()
