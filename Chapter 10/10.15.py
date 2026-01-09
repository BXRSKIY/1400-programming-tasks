import random

def simulate(trials: int):
    counts = [0]*7  # индексы 1..6
    for _ in range(trials):
        x = random.randint(1, 6)
        counts[x] += 1
    freqs = [counts[i]/trials for i in range(1,7)]
    return freqs

def main():
    # 10.15. Относительные частоты появления 1..6 при 100 и 1000 бросках.
    f100 = simulate(100)
    f1000 = simulate(1000)
    print("100 бросков:", *f100)
    print("1000 бросков:", *f1000)


if __name__ == "__main__":
    main()
