def main():
    import sys
    # Масса каждого человека в группе (все числа входа).
    masses = list(map(float, sys.stdin.read().split()))
    fat = [m for m in masses if m > 100]
    others = [m for m in masses if m <= 100]
    avg_fat = sum(fat) / len(fat) if fat else 0.0
    avg_others = sum(others) / len(others) if others else 0.0
    print(avg_fat, avg_others)


if __name__ == "__main__":
    main()
