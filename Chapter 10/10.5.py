import random

def main():
    # 10.5. 30 целых 0..5, выводим только нечётные.
    res = []
    for _ in range(30):
        x = random.randint(0, 5)
        if x % 2 == 1:
            res.append(x)
    print(*res)


if __name__ == "__main__":
    main()
