def main():
    import sys
    # Формат: n, затем для каждой команды два числа: выигрыши и проигрыши.
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + 2*n:
        raise ValueError(f"Ожидается 2*{n} чисел для команд")
    vals = data[1:1+2*n]
    count = 0
    for i in range(0, len(vals), 2):
        wins = vals[i]
        losses = vals[i+1]
        if wins > losses:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
