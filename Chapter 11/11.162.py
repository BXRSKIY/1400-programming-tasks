def main():
    # 11.162. В массиве — рост 25 учеников (в порядке убывания).
    # Из класса выбыли несколько учеников.
    # Составить массив ростов оставшихся.
    # Рассмотреть:
    # 1) известны порядковые номера выбывших;
    # 2) известны значения роста выбывших.
    #
    # Формат ввода (один из возможных вариантов):
    # 25 значений роста,
    # p — количество выбывших по номерам,
    # p номеров (1-базных),
    # q — количество выбывших по росту,
    # q значений роста.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 26:
        return
    heights = data[:25]
    idx = 25
    if idx >= len(data):
        print("case1:", *heights)
        print("case2:", *heights)
        return
    p = int(data[idx]); idx += 1
    nums = [int(x) for x in data[idx:idx+p]]; idx += p
    if idx >= len(data):
        q = 0
        vals = []
    else:
        q = int(data[idx]); idx += 1
        vals = data[idx:idx+q]

    def delete_at(a, pos):
        b = a[:]
        if 0 <= pos < len(b):
            for i in range(pos, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0.0
        return b

    # 1) по номерам (удаляем по возрастанию индексов, с поправкой на сдвиги)
    arr1 = heights[:]
    for k in sorted(nums):
        arr1 = delete_at(arr1, k-1)
    print("case1:", *arr1)

    # 2) по значениям роста (для каждого значения удаляем первое вхождение)
    arr2 = heights[:]
    for h in vals:
        try:
            pos = arr2.index(h)
        except ValueError:
            continue
        arr2 = delete_at(arr2, pos)
    print("case2:", *arr2)


if __name__ == "__main__":
    main()
