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
    # 11.18. Заполнить массив:
    # а) двадцатью первыми натуральными числами, делящимися на 13 или на 17
    #    и находящимися в интервале с левой границей 300;
    # б) тридцатью первыми простыми числами.
    a_arr = []
    x = 300
    while len(a_arr) < 20:
        if x % 13 == 0 or x % 17 == 0:
            a_arr.append(x)
        x += 1

    b_arr = []
    y = 2
    while len(b_arr) < 30:
        if is_prime(y):
            b_arr.append(y)
        y += 1

    print("a)", *a_arr)
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
