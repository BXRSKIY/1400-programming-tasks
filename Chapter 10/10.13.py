import random

def throw_die():
    return random.randint(1, 6)

def main():
    # 10.13. Игра: два участника бросают кубик.
    # 1) каждый бросает два раза, побеждает больший суммарный результат.
    a1 = throw_die()
    a2 = throw_die()
    b1 = throw_die()
    b2 = throw_die()
    sa = a1 + a2
    sb = b1 + b2
    print("Игрок 1 броски:", a1, a2, "сумма", sa)
    print("Игрок 2 броски:", b1, b2, "сумма", sb)
    if sa > sb:
        print("Игрок 1 выиграл")
    elif sb > sa:
        print("Игрок 2 выиграл")
    else:
        print("Ничья")

    # 2) многократные игры, считаем количество выигрышей
    games = int(input("Сколько партий сыграть? ").strip())
    wins1 = wins2 = draws = 0
    for _ in range(games):
        a = throw_die()
        b = throw_die()
        if a > b:
            wins1 += 1
        elif b > a:
            wins2 += 1
        else:
            draws += 1
    print("Результат серии:")
    print("Игрок 1 выиграл", wins1, "раз(а)")
    print("Игрок 2 выиграл", wins2, "раз(а)")
    print("Ничьих:", draws)


if __name__ == "__main__":
    main()
