def main():
    import sys
    # Мощности двигателей 30 моделей.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 30:
        raise ValueError("Ожидается 30 значений")
    powers = data[:30]
    cond = any(p > 200 for p in powers)
    print("YES" if cond else "NO")


if __name__ == "__main__":
    main()
