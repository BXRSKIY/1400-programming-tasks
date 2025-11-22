def main():
    import sys
    # Рост учеников: мальчики — отрицательные, девочки — положительные.
    hs = list(map(float, sys.stdin.read().split()))
    boys = [-h for h in hs if h < 0]
    girls = [h for h in hs if h > 0]
    avg_b = sum(boys) / len(boys) if boys else 0.0
    avg_g = sum(girls) / len(girls) if girls else 0.0
    print(avg_b, avg_g)


if __name__ == "__main__":
    main()
