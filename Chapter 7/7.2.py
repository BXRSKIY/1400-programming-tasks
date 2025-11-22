def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 11:
        raise ValueError("Ожидается n и 10 чисел a1..a10")
    # первое число — n (натуральное), далее 10 вещественных чисел
    n = int(data[0])
    a = data[1:11]
    print(sum(a))


if __name__ == "__main__":
    main()
