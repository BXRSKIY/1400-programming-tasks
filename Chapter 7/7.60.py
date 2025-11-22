def main():
    import sys
    # Температура воздуха в течение месяца (любое количество значений).
    temps = list(map(float, sys.stdin.read().split()))
    count = sum(1 for t in temps if t < 0)
    print(count)


if __name__ == "__main__":
    main()
