import random

def ask_once():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    print(f"Чему равно произведение {a} × {b}?")
    ans = int(input().strip())
    correct = (ans == a * b)
    if correct:
        print("Верно")
    else:
        print("Неверно, правильный ответ:", a*b)
    return correct

def main():
    # 10.18. Тренажёр таблицы умножения.
    # а) один вопрос
    print("Вариант а):")
    ask_once()

    # б) 20 вопросов, подсчёт правильных/неправильных
    print("Вариант б):")
    correct = 0
    total = 20
    for _ in range(total):
        if ask_once():
            correct += 1
    print("Правильных:", correct, "Неправильных:", total - correct)

    # в) до ответа 0
    print("Вариант в):")
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print(f"Чему равно произведение {a} × {b}? (0 для выхода)")
        ans = int(input().strip())
        if ans == 0:
            break
        if ans == a * b:
            print("Верно")
        else:
            print("Неверно, правильный ответ:", a*b)


if __name__ == "__main__":
    main()
