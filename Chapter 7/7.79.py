def main():
    import sys
    # Вход: очки P и количество игр G.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются P и G")
    P, G = data[0], data[1]
    solutions = []
    for w in range(G+1):
        for d in range(G-w+1):
            l = G - w - d
            if 3*w + d == P and l >= 0:
                solutions.append((w, d, l))
    # Выведем все возможные тройки построчно.
    if not solutions:
        print("NO")
    else:
        for w, d, l in solutions:
            print(w, d, l)


if __name__ == "__main__":
    main()
