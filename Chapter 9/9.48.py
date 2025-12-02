def prime_factors(n: int):
    # возвращает список простых множителей с кратностями
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def main():
    n = int(input())
    fs = prime_factors(n)
    # 1) каждый простой множитель по одному разу
    unique_fs = sorted(set(fs))
    print("variant1:", *unique_fs)
    # 2) каждый множитель столько раз, сколько он входит
    print("variant2:", *fs)


if __name__ == "__main__":
    main()
