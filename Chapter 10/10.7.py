import random

def main():
    # 10.7.
    # а) два разных целых a,b: 0 <= a < 2, 0 <= b < 3
    while True:
        a = random.randint(0, 1)
        b = random.randint(0, 2)
        if a != b:
            break
    print("a =", a, "b =", b)

    # б) три разных целых a,b,c: 1<=a<3, 0<=b<3, 1<=c<4
    while True:
        a = random.randint(1, 2)
        b = random.randint(0, 2)
        c = random.randint(1, 3)
        if len({a, b, c}) == 3:
            break
    print("a =", a, "b =", b, "c =", c)

    # в) 15 чисел: 7 двоек и 8 троек в случайном порядке
    arr = [2]*7 + [3]*8
    random.shuffle(arr)
    print(*arr)


if __name__ == "__main__":
    main()
