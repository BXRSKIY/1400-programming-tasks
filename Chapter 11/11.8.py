def main():
    # 11.8. Вывод на экран любого элемента массива по его индексу.
    # Формат ввода:
    # сначала массив (произвольное количество чисел),
    # затем индекс i (0-based).
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    # последний элемент считаем индексом
    idx = int(data[-1])
    arr = data[:-1]
    if 0 <= idx < len(arr):
        print(arr[idx])
    else:
        print("Index out of range")


if __name__ == "__main__":
    main()
