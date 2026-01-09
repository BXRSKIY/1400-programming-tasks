import random

def main():
    # 10.12. Два игрока бросают по одному кубику, вывести, кто получил больше очков.
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print("Игрок 1:", a)
    print("Игрок 2:", b)
    if a > b:
        print("Победил игрок 1")
    elif b > a:
        print("Победил игрок 2")
    else:
        print("Ничья")


if __name__ == "__main__":
    main()
