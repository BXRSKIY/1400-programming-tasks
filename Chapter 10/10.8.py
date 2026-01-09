import random

def main():
    # 10.8. Подбрасывание монеты: 0 или 1.
    x = random.randint(0, 1)
    if x == 0:
        print("0 (решка)")
    else:
        print("1 (орел)")


if __name__ == "__main__":
    main()
