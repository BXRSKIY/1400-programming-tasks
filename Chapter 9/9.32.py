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
        # Найти натуральное число из интервала [a, b] с максимальной суммой делителей.
        a, b = map(int, input().split())
        best_n = a
        best_sum = sum_divisors(a, proper=False)
        for n in range(a + 1, b + 1):
            s = sum_divisors(n, proper=False)
            if s > best_sum:
                best_sum = s
                best_n = n
        print(best_n)


    if __name__ == "__main__":
        main()
