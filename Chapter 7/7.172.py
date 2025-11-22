def main():
    import sys
    times = list(map(float, sys.stdin.read().split()))
    if len(times) < 22:
        raise ValueError("Ожидается 22 результата")
    times = times[:22]
    # найдём три наименьших результата (время)
    best = sorted(times)[:3]
    # выводим три результата по возрастанию
    print(*best)


if __name__ == "__main__":
    main()
