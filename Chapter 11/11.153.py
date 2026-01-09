def main():
    # 11.153. Одномерный массив из 20 элементов.
    # Переставить первые три и последние три элемента,
    # сохранив порядок их следования в своих тройках.
    import sys
    arr = sys.stdin.read().split()
    if len(arr) < 6:
        print(*arr)
        return
    first3 = arr[:3]
    last3 = arr[-3:]
    middle = arr[3:-3]
    res = last3 + middle + first3
    print(*res)


if __name__ == "__main__":
    main()
