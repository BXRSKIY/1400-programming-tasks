import random

def draw_card():
    suits = ["пики", "трефы", "бубны", "червы"]
    ranks = ["шестерка", "семерка", "восьмерка", "девятка",
             "десятка", "валет", "дама", "король", "туз"]
    return random.choice(ranks), random.choice(suits)

def compare_cards(c1, c2):
    ranks = ["шестерка", "семерка", "восьмерка", "девятка",
             "десятка", "валет", "дама", "король", "туз"]
    suits = ["пики", "трефы", "бубны", "червы"]
    rank_value = {r:i for i,r in enumerate(ranks)}
    suit_value = {s:i for i,s in enumerate(suits)}
    (r1,s1) = c1
    (r2,s2) = c2
    if rank_value[r1] > rank_value[r2]:
        return 1
    if rank_value[r2] > rank_value[r1]:
        return -1
    if suit_value[s1] > suit_value[s2]:
        return 1
    if suit_value[s2] > suit_value[s1]:
        return -1
    return 0

def main():
    # 10.22. Многократная игра по условиям 10.21
    games = int(input("Сколько раз играть? ").strip())
    wins1 = wins2 = draws = 0
    for _ in range(games):
        c1 = draw_card()
        c2 = draw_card()
        res = compare_cards(c1, c2)
        if res > 0:
            wins1 += 1
        elif res < 0:
            wins2 += 1
        else:
            draws += 1
    print("Игрок 1 выиграл", wins1, "раз(а)")
    print("Игрок 2 выиграл", wins2, "раз(а)")
    print("Ничьих:", draws)


if __name__ == "__main__":
    main()
