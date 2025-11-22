def main():
    import sys
    # Осадки за каждый день февраля (28 значений).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 28:
        raise ValueError("Ожидается 28 значений осадков")
    rains = data[:28]
    even_sum = 0.0
    odd_sum = 0.0
    for day, val in enumerate(rains, start=1):
        if day % 2 == 0:
            even_sum += val
        else:
            odd_sum += val
    print("YES" if even_sum > odd_sum else "NO")


if __name__ == "__main__":
    main()
