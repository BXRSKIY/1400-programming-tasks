def main():
    import sys
    # Возраст 20 учеников первого класса и 20 второго.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 40:
        raise ValueError("Ожидается 40 значений возраста")
    class1 = data[:20]
    class2 = data[20:40]
    avg1 = sum(class1) / 20.0
    avg2 = sum(class2) / 20.0
    print(avg1, avg2)


if __name__ == "__main__":
    main()
