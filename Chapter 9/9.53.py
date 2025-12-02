def main():
    # Найти наименьшее натуральное n, которое можно представить
    # двумя различными способами в виде суммы кубов двух натуральных чисел.
    # Ищем по всем a,b <= 50, этого достаточно (ответ 1729).
    from collections import defaultdict
    sums = defaultdict(list)
    limit = 50
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            s = a**3 + b**3
            sums[s].append((a, b))
    candidates = [s for s, pairs in sums.items() if len(pairs) >= 2]
    if not candidates:
        print(0)
        return
    n = min(candidates)
    print(n)
    # дополнительно можно вывести сами представления
    for a, b in sums[n][:2]:
        print(a, b)


if __name__ == "__main__":
    main()
