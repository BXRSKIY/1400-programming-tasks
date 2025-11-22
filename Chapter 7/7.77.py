def main():
    # Вход: пары (номер_команды, время_удаления).
    # Номер команды 1 или 2. Ноль вместо номера — конец игры.
    team1_count = team2_count = 0
    team1_time = team2_time = 0
    while True:
        try:
            team = int(input())
        except EOFError:
            break
        if team == 0:
            break
        minutes = int(input())
        if team == 1:
            team1_count += 1
            team1_time += minutes
        elif team == 2:
            team2_count += 1
            team2_time += minutes
    print(team1_count, team1_time)
    print(team2_count, team2_time)


if __name__ == "__main__":
    main()
