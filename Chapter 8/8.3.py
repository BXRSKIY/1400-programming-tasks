def main():
    # Дано число a (0 < a <= 1).
    # Из чисел 1, 1/2, 1/3, ... напечатать те, которые не меньше a.
    a = float(input())
    denom = 1
    while True:
        value = 1.0 / denom
        if value >= a:
            print(value)
            denom += 1
        else:
            break


if __name__ == "__main__":
    main()
