import math

def main():
    # 11.40. Дан массив. Составить программу расчета:
    # а) квадратного корня из любого элемента массива;
    # б) среднего арифметического двух любых элементов массива.
    #
    # Формат ввода:
    # сначала индексы i, j (для среднего),
    # затем элементы массива.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        return
    i = int(data[0])  # индекс для корня (номер элемента с 1)
    j = int(data[1])  # второй индекс для среднего (также 1-базный)
    arr = data[2:]
    if not arr:
        return
    idx_i = i - 1
    idx_j = j - 1
    if 0 <= idx_i < len(arr):
        if arr[idx_i] >= 0:
            print("sqrt:", math.sqrt(arr[idx_i]))
        else:
            print("sqrt: NaN")
    else:
        print("sqrt: index out of range")
    if 0 <= idx_i < len(arr) and 0 <= idx_j < len(arr):
        avg = (arr[idx_i] + arr[idx_j]) / 2.0
        print("avg:", avg)
    else:
        print("avg: index out of range")


if __name__ == "__main__":
    main()
