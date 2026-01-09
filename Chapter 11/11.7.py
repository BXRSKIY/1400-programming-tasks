import random

def main():
    # 11.7. Заполнить массив из n элементов случайными целыми
    # числами из интервала [a,b] включительно.
    n, a, b = map(int, input().split())
    arr = [random.randint(a, b) for _ in range(n)]
    print(*arr)


if __name__ == "__main__":
    main()
