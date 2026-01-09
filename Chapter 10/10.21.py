import random

def main():
    # 10.21. Два игрока выбирают по карте, определить, чья старше.
    suits = ["пики", "трефы", "бубны", "червы"]
    ranks = ["шестерка", "семерка", "восьмерка", "девятка",
             "десятка", "валет", "дама", "король", "туз"]
    # масти и ранги упорядочены по возрастанию старшинства

    def draw_card():
        return random.choice(ranks), random.choice(suits)

    r1, s1 = draw_card()
    r2, s2 = draw_card()
    print(f"Игрок 1: {r1} {s1}")
    print(f"Игрок 2: {r2} {s2}")

    rank_value = {r:i for i,r in enumerate(ranks)}
    suit_value = {s:i for i,s in enumerate(suits)}

    if rank_value[r1] > rank_value[r2]:
        print("Победил игрок 1")
    elif rank_value[r2] > rank_value[r1]:
        print("Победил игрок 2")
    else:
        # ранги равны, смотрим масть
        if suit_value[s1] > suit_value[s2]:
            print("Победил игрок 1 (масть старше)")
        elif suit_value[s2] > suit_value[s1]:
            print("Победил игрок 2 (масть старше)")
        else:
            print("Полная ничья")


if __name__ == "__main__":
    main()
