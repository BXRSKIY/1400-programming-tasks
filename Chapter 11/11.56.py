def main():
    # 11.56. В массиве хранится информация о баллах, полученных
    # спортсменом-десятиборцем в каждом из десяти видов спорта.
    # Для выхода в следующий этап нужно набрать не менее порогового
    # числа баллов, которое мы считаем введённым последним числом.
    #
    # Формат ввода:
    # b1 b2 ... b10 T
    # bi — баллы в видах, T — порог.
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 11:
        raise ValueError("Ожидается не менее 11 целых чисел (10 баллов + порог).")
    scores = data[:10]
    threshold = data[10]
    total = sum(scores)
    print("YES" if total >= threshold else "NO")


if __name__ == "__main__":
    main()
