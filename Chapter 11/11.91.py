def main():
    # 11.91. Масса каждого из 25 человек хранится в массиве.
    # Людей с массой > 100 кг считаем полными (есть хотя бы один такой).
    # Определить среднюю массу полных людей и среднюю массу остальных.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    masses = arr[:25]
    fat = [x for x in masses if x > 100]
    others = [x for x in masses if x <= 100]
    avg_fat = sum(fat) / len(fat) if fat else 0.0
    avg_others = sum(others) / len(others) if others else 0.0
    print(avg_fat, avg_others)


if __name__ == "__main__":
    main()
