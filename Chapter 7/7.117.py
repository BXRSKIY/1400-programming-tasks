def main():
    import sys
    # Рост: мальчики <0, девочки >0. Проверить, превосходит ли
    # средний рост мальчиков средний рост девочек более чем на 10 см.
    hs = list(map(float, sys.stdin.read().split()))
    boys = [-h for h in hs if h < 0]
    girls = [h for h in hs if h > 0]
    if not boys or not girls:
        print("NO")
        return
    avg_b = sum(boys) / len(boys)
    avg_g = sum(girls) / len(girls)
    print("YES" if avg_b > avg_g + 10 else "NO")


if __name__ == "__main__":
    main()
