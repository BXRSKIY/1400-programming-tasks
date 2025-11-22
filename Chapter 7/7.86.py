def main():
    import sys
    # Формат: n, затем n целых ci
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} целых чисел")
    c = data[1:1+n]
    cnt = sum(1 for x in c if x < 20)
    print("YES" if cnt == 5 else "NO")


if __name__ == "__main__":
    main()
