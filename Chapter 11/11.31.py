def main():
    # 11.31. Дан массив. Вывести на экран сначала его элементы,
    # стоящие на четных местах, затем – на нечетных.
    # Места считаем с 1: 2-й,4-й,... — четные.
    import sys
    arr = sys.stdin.read().split()
    even_pos = [arr[i] for i in range(1, len(arr), 2)]
    odd_pos = [arr[i] for i in range(0, len(arr), 2)]
    print("even_positions:", *even_pos)
    print("odd_positions:", *odd_pos)


if __name__ == "__main__":
    main()
