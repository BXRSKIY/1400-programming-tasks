import random

def main():
    # 11.20. Проверка знания таблицы умножения.
    # На экран по одному выводится 20 вопросов вида "a*b", множители 2..9,
    # пользователь вводит ответ, ответы записываются в массив.
    answers = []
    for _ in range(20):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        print(f"Чему равно произведение {a} на {b}?")
        try:
            ans = int(input())
        except ValueError:
            ans = None
        answers.append(ans)
    print("Введенные ответы:")
    print(*answers)


if __name__ == "__main__":
    main()
