def main():
    # Дано число a (0 < a <= 1).
    # Среди чисел 1, 1/2, 1/3, ... найти первое число, которое меньше a.
    a = float(input())
    denom = 1
    while True:
        value = 1.0 / denom
        if value < a:
            print(value)
            break
        denom += 1


if __name__ == "__main__":
    main()
