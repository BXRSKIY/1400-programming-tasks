def main():
    import sys
    # Осадки за каждый день марта (31 день).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 31:
        raise ValueError("Ожидается 31 значение")
    rains = data[:31]
    zero_days = sum(1 for r in rains if r == 0)
    print("YES" if zero_days == 10 else "NO")


if __name__ == "__main__":
    main()
