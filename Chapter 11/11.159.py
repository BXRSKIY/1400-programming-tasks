def main():
    # 11.159. В массиве — рост 25 учеников в порядке убывания.
    # Один ученик выбыл. Составить массив ростов оставшихся.
    # Рассмотреть два случая:
    # 1) известен порядковый номер выбывшего;
    # 2) известен рост выбывшего.
    #
    # Формат ввода:
    # 25 значений роста,
    # затем k (номер выбывшего),
    # затем h (рост выбывшего).
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 27:
        return
    heights = data[:25]
    k = int(data[25])
    h = data[26]

    def delete_at(a, idx):
        b = a[:]
        if 0 <= idx < len(b):
            for i in range(idx, len(b)-1):
                b[i] = b[i+1]
            b[-1] = 0.0
        return b

    # 1) по номеру
    arr1 = delete_at(heights, k-1)
    print("case1:", *arr1)

    # 2) по росту (удаляем первое вхождение)
    try:
        idx = heights.index(h)
    except ValueError:
        # если такого роста нет — оставляем без изменений
        arr2 = heights[:]
    else:
        arr2 = delete_at(heights, idx)
    print("case2:", *arr2)


if __name__ == "__main__":
    main()
