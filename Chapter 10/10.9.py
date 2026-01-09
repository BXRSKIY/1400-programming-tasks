import random

def simulate(trials: int):
    c0 = c1 = 0
    for _ in range(trials):
        x = random.randint(0, 1)
        if x == 0:
            c0 += 1
        else:
            c1 += 1
    return c0 / trials, c1 / trials

def main():
    # 10.9. Относительная частота 0 и 1 при 100 и 1000 подбрасываниях.
    f0_100, f1_100 = simulate(100)
    f0_1000, f1_1000 = simulate(1000)
    print("100 tosses:", f0_100, f1_100)
    print("1000 tosses:", f0_1000, f1_1000)


if __name__ == "__main__":
    main()
