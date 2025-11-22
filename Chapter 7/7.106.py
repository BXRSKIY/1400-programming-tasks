def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 16:
        raise ValueError("Ожидается 16 вещественных чисел c1..c16")
    c = data[:16]
    above = [x for x in c if x > 20]
    if not above:
        raise ValueError("По условию должны быть числа > 20")
    print(sum(above) / len(above))


if __name__ == "__main__":
    main()
