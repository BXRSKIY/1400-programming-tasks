def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    n = int(data[0])
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел t1..tn")
    t = data[1:1+n]
    c = []
    total = 0.0
    min_t = t[0]
    min_pos = 1
    for i, val in enumerate(t, start=1):
        total += val
        c.append(total)
        if val <= min_t:
            min_t = val
            min_pos = i
    # выводим все c_i в одну строку, затем номер покупателя
    print(*c)
    print(min_pos)


if __name__ == "__main__":
    main()
