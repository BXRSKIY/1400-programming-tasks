def main():
    import sys
    # Формат: m, затем m целых d1..dm
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    m = data[0]
    if len(data) < 1 + m:
        raise ValueError(f"Ожидается m={m} целых чисел")
    d = data[1:1+m]
    pos_cnt = sum(1 for x in d if x > 0)
    print("YES" if pos_cnt % 3 == 0 else "NO")


if __name__ == "__main__":
    main()
