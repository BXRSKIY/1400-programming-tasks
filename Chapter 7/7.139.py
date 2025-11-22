def main():
    import sys
    # Максимальные скорости 20 марок автомобилей.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 скоростей")
    v = data[:20]
    print(max(v))


if __name__ == "__main__":
    main()
