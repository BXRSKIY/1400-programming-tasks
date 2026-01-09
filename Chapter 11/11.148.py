def main():
    # 11.148. Дан массив. Сравнить первый и второй элементы.
    # Если второй меньше первого — поменять их местами.
    # Затем то же самое проделать для 2-го и 3-го, 3-го и 4-го и т.д.
    # Какое число окажется в результате в последнем элементе массива?
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    n = len(arr)
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr[-1] if arr else "")


if __name__ == "__main__":
    main()
