import random

def main():
    # 10.3. Получить случайные m, n (<=20), n целых [a,b], m вещественных [0,n].
    a, b = map(int, input().split())
    m = random.randint(1, 20)
    n = random.randint(1, 20)
    print("m =", m, "n =", n)
    print("Integers:")
    for _ in range(n):
        print(random.randint(a, b))
    print("Reals:")
    for _ in range(m):
        print(random.random() * n)


if __name__ == "__main__":
    main()
