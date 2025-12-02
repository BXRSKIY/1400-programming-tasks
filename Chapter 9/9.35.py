def pay_minimal(sum_value: int):
    # Купюры 64,32,16,8,4,2,1 — жадный алгоритм даёт минимум.
    denoms = [64, 32, 16, 8, 4, 2, 1]
    counts = []
    remaining = sum_value
    for d in denoms:
        c = remaining // d
        counts.append(c)
        remaining -= c * d
    return denoms, counts


def main():
    # Дано n. Для сумм n..n+10 найти минимальное количество купюр
    # (1,2,4,8,16,32,64) и указать их количество.
    n = int(input())
    for s in range(n, n + 11):
        denoms, counts = pay_minimal(s)
        # вывод: сумма и далее пары d:count для ненулевых
        parts = [f"sum={s}"]
        for d, c in zip(denoms, counts):
            if c:
                parts.append(f"{d}:{c}")
        print(" ".join(parts))


if __name__ == "__main__":
    main()
