def main():
    import sys
    # Формат: n (натуральное, но фактически не используется), затем 15 вещественных чисел.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 16:
        raise ValueError("Ожидается n и 15 вещественных чисел")
    n = int(data[0])
    x = data[1:16]
    mx = max(x)
    mn = min(x)
    print(mx)
    print(mn)
    print(mx, mn)


if __name__ == "__main__":
    main()
