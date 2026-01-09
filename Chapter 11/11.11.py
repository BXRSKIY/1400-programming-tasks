def main():
    # 11.11. Заполнить массив 25 первыми натуральными числами (1..25),
    # затем добавить в него числа 100 и 200.
    arr = list(range(1, 26))
    arr.append(100)
    arr.append(200)
    print(*arr)


if __name__ == "__main__":
    main()
