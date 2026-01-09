def main():
    # 11.63. Осадки за каждый месяц года (12 чисел).
    # Найти общее число осадков, выпавших в марте, июне, сентябре и декабре.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if len(arr) < 12:
        arr += [0.0] * (12 - len(arr))
    # месяцы 3,6,9,12 => индексы 2,5,8,11
    s = arr[2] + arr[5] + arr[8] + arr[11]
    print(s)


if __name__ == "__main__":
    main()
