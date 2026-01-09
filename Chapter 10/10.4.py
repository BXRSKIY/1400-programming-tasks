import random

def main():
    # 10.4. 50 целых 0..3, но выводим только 0 и 1.
    res = []
    for _ in range(50):
        x = random.randint(0, 3)
        if x in (0, 1):
            res.append(x)
    print(*res)


if __name__ == "__main__":
    main()
