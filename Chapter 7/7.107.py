def main():
    import sys
    # Формат: n (порог), затем 12 целых a1..a12.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 13:
        raise ValueError("Ожидается порог и 12 целых чисел")
    threshold = data[0]
    a = data[1:13]
    above = [x for x in a if x > threshold]
    if not above:
        raise ValueError("По условию должны быть числа > n")
    print(sum(above) / len(above))


if __name__ == "__main__":
    main()
