import random

def single_round():
    # 1 = odd, 2 = even
    guess = int(input("Чет (введите 2) или нечет (введите 1)? ").strip())
    x = random.randint(0, 1000000)
    parity = 2 if x % 2 == 0 else 1
    print("Число компьютера:", x)
    if guess == parity:
        print("Вы угадали!")
        return True
    else:
        print("Вы не угадали.")
        return False

def main():
    # Вариант а): одна попытка
    print("Вариант а):")
    single_round()

    # Вариант б): n попыток, считаем счёт
    print("Вариант б):")
    n = int(input("Сколько раз играть? ").strip())
    user_wins = comp_wins = 0
    for _ in range(n):
        if single_round():
            user_wins += 1
        else:
            comp_wins += 1
    print(f"Счет {user_wins}:{comp_wins} ", end="")
    if user_wins > comp_wins:
        print("в вашу пользу. Вы выиграли!")
    elif comp_wins > user_wins:
        print("в пользу компьютера. Вы проиграли!")
    else:
        print("ничья.")

    # Вариант в): до ответа «Нет»
    print("Вариант в):")
    user_ok = comp_ok = 0
    while True:
        if single_round():
            user_ok += 1
        else:
            comp_ok += 1
        ans = input("Продолжить еще раз? (Да/Нет): ").strip().lower()
        if ans.startswith("н"):
            break
    print("Верных ответов:", user_ok, "Неверных:", comp_ok)


if __name__ == "__main__":
    main()
