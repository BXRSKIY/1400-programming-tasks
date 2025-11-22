def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 10:
        raise ValueError("Ожидается 10 вещественных чисел")
    s = sum(data[:10])
    # Верно ли, что сумма превышает 100.78?
    print("YES" if s > 100.78 else "NO")


if __name__ == "__main__":
    main()
