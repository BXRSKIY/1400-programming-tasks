def main():
    # 11.79. Результаты 20 игр футбольной команды:
    # 3 - выигрыш, 2 - проигрыш, 1 - ничья.
    # Определить количество выигрышей, ничьих и проигрышей.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    games = arr[:20]
    wins = sum(1 for x in games if x == 3)
    losses = sum(1 for x in games if x == 2)
    draws = sum(1 for x in games if x == 1)
    print("wins:", wins)
    print("draws:", draws)
    print("losses:", losses)


if __name__ == "__main__":
    main()
