def main():
    import sys
    # 20 однозначных или двузначных чисел: xy => x забито, y пропущено.
    # 0 => 0:0.
    nums = list(map(int, sys.stdin.read().split()))
    if len(nums) < 20:
        raise ValueError("Ожидается 20 чисел")
    games = []
    for v in nums[:20]:
        if v == 0:
            scored = conceded = 0
        else:
            scored = v // 10
            conceded = v % 10
        games.append((scored, conceded))
    wins = draws = losses = 0
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
    print(wins)
    print(wins, losses)
    print(wins, draws, losses)


if __name__ == "__main__":
    main()
