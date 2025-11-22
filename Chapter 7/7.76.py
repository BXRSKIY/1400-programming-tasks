def main():
    import sys
    # Вход: 24 пары (номер_команды, время_удаления).
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 48:
        raise ValueError("Ожидается 24 пары значений (команда, минуты)")
    team1_count = team2_count = 0
    team1_time = team2_time = 0
    for i in range(0, 48, 2):
        team = data[i]
        minutes = data[i+1]
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
