import random

def main():
    # 11.21*. Заполнить массив из 20 элементов неповторяющимися числами.
    # Возьмем числа из диапазона 1..100.
    arr = []
    while len(arr) < 20:
        x = random.randint(1, 100)
        if x not in arr:
            arr.append(x)
    print(*arr)


if __name__ == "__main__":
    main()
