import random

def main():
    # 10.6. 50 целых 0 или 1, подсчитать количество.
    zeros = ones = 0
    for _ in range(50):
        x = random.randint(0, 1)
        if x == 0:
            zeros += 1
        else:
            ones += 1
    print("zeros =", zeros, "ones =", ones)


if __name__ == "__main__":
    main()
