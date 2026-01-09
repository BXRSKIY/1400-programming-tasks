import math

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True

def main():
    # 11.19. Начиная с числа 100, найти первые 10 простых чисел и записать их в массив.
    arr = []
    x = 100
    while len(arr) < 10:
        if is_prime(x):
            arr.append(x)
        x += 1
    print(*arr)


if __name__ == "__main__":
    main()
