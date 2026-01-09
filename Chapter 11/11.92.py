def main():
    # 11.92. Рост 22 учеников: рост мальчиков задан отрицательными числами,
    # девочек — положительными. Определить средний рост мальчиков и девочек.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    heights = arr[:22]
    boys = [-x for x in heights if x < 0]
    girls = [x for x in heights if x > 0]
    avg_boys = sum(boys) / len(boys) if boys else 0.0
    avg_girls = sum(girls) / len(girls) if girls else 0.0
    print(avg_boys, avg_girls)


if __name__ == "__main__":
    main()
