import random

def main():
    # 11.5. Массив для хранения ростов 12 человек.
    # Заполнить целыми значениями в диапазоне [163,190].
    arr = [random.randint(163, 190) for _ in range(12)]
    print(*arr)


if __name__ == "__main__":
    main()
