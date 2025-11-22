def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n or n < 4:
        raise ValueError(f"Ожидается n={n} (>=4) результатов")
    a = data[1:1+n]
    # выберем 4 минимальных значения
    # сохраним также их индексы (1-based)
    indexed = list(enumerate(a, start=1))
    indexed.sort(key=lambda t: t[1])
    chosen = indexed[:4]
    # вывод: индексы и результаты, например
    indices = [i for i, _ in chosen]
    results = [v for _, v in chosen]
    print(*indices)
    print(*results)


if __name__ == "__main__":
    main()
