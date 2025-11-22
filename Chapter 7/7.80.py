def main():
    import sys
    # 20 пар (забито, пропущено)
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 40:
        raise ValueError("Ожидается 20 пар чисел")
    games = []
    for i in range(0, 40, 2):
        scored = data[i]
        conceded = data[i+1]
        games.append((scored, conceded))
    wins = draws = losses = 0
    # а) печать результата каждой игры
    results = []
    for scored, conceded in games:
        if scored > conceded:
            results.append("выигрыш")
            wins += 1
        elif scored == conceded:
            results.append("ничья")
            draws += 1
        else:
            results.append("проигрыш")
            losses += 1
    print(*results, sep=" ")
    # б) количество выигрышей
    print(wins)
    # в) количество выигрышей и проигрышей
    print(wins, losses)
    # г) выигрыши, ничьи, проигрыши
    print(wins, draws, losses)


if __name__ == "__main__":
    main()
