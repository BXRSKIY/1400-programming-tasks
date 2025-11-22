def main():
    import sys
    # Количество осадков за каждый день февраля (28 значений),
    # затем общее количество осадков в прошлом году (одно число).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 29:
        raise ValueError("Ожидается 28 значений и одно сравниваемое число")
    current = data[:28]
    last_year = data[28]
    s_current = sum(current)
    print("YES" if s_current > last_year else "NO")


if __name__ == "__main__":
    main()
