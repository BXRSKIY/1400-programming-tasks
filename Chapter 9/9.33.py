    def sum_divisors(n: int, proper: bool = False) -> int:
    """Возвращает сумму делителей числа n.
    Если proper=True, не включает само число n."""
    s = 1 if n > 1 else 0
    # начинаем с 2, чтобы 1 уже была учтена (для n>1)
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            s += d
            other = n // d
            if other != d:
                s += other
    if not proper and n > 1:
        s += n
    return s

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

    def main():
        # Найти все пары натуральных дружественных чисел, меньших 50000.
        limit = 50000
        # Суммы собственных делителей
        sd = [0] * limit
        for n in range(1, limit):
            sd[n] = sum_divisors(n, proper=True)
        for a in range(2, limit):
            b = sd[a]
            if b > a and b < limit and sd[b] == a:
                print(a, b)


    if __name__ == "__main__":
        main()
