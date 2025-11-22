def main():
    import sys
    # Осадки за каждый день января и марта (по 31 дню).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 62:
        raise ValueError("Ожидается 62 значения (31 для января, 31 для марта)")
    jan = data[:31]
    mar = data[31:62]
    avg_jan = sum(jan) / 31.0
    avg_mar = sum(mar) / 31.0
    print(avg_jan, avg_mar)


if __name__ == "__main__":
    main()
