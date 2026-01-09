def main():
    # 11.114. Стоимость 50 марок автомобилей.
    # Найти стоимость самого дорогого.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    cars = arr[:50]
    if not cars:
        print(0.0)
    else:
        print(max(cars))


if __name__ == "__main__":
    main()
