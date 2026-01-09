import random

def main():
    # 10.14. Три игрока бросают K игральных кубиков, у кого сумма больше.
    K = int(input("K: ").strip())
    sums = []
    for player in range(3):
        s = 0
        for _ in range(K):
            s += random.randint(1, 6)
        sums.append(s)
        print(f"Игрок {player+1}: сумма = {s}")
    max_sum = max(sums)
    winners = [i+1 for i,s in enumerate(sums) if s == max_sum]
    if len(winners) == 1:
        print("Победил игрок", winners[0])
    else:
        print("Ничья между игроками:", *winners)


if __name__ == "__main__":
    main()
