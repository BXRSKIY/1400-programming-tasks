import random

def main():
    # 11.6. Массив для хранения весов 20 человек.
    # Заполнить целыми значениями в диапазоне [50,100].
    arr = [random.randint(50, 100) for _ in range(20)]
    print(*arr)


if __name__ == "__main__":
    main()
