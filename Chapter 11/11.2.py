def main():
    # 11.2. Заполнить массив из десяти элементов значениями,
    # вводимыми с клавиатуры.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    # берем первые 10 значений (если их меньше, используем только имеющиеся)
    arr = data[:10]
    print(*arr)


if __name__ == "__main__":
    main()
