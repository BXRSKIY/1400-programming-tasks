def main():
    # 11.173. Данные о росте 25 учеников класса, упорядоченные по
    # убыванию, записаны в массиве. В начале учебного года в класс пришли
    # новые ученики. Составить массив, учитывающий рост новых учеников.
    # Рассмотреть два случая:
    # 1) известны порядковые номера новых учеников;
    # 2) известны значения роста новых учеников.
    #
    # Один из возможных вариантов формата ввода:
    # 25 ростов (по убыванию),
    # p — число новых учеников с известными номерами,
    # p номеров (1..N),
    # q — число новых учеников с известными ростами,
    # q значений роста.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 26:
        return
    heights = data[:25]
    idx = 25
    p = int(data[idx]); idx += 1
    nums = [int(x) for x in data[idx:idx+p]]; idx += p
    if idx >= len(data):
        q = 0
        vals = []
    else:
        q = int(data[idx]); idx += 1
        vals = data[idx:idx+q]

    # 1) вставка по номерам (без соблюдения сортировки)
    arr1 = heights[:]
    shift = 0
    for k in nums:
        pos = max(1, min(len(arr1)+1, int(k)))
        arr1.insert(pos-1, 0.0)  # рост можно задать отдельно
    print("case1:", *arr1)

    # 2) вставка по ростам с сохранением убывания
    arr2 = heights[:]
    for h in vals:
        pos = len(arr2)
        for i, x in enumerate(arr2):
            if h > x:
                pos = i
                break
        arr2.insert(pos, h)
    print("case2:", *arr2)


if __name__ == "__main__":
    main()
