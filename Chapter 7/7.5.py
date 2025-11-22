def main():
    import sys
    # Зарплаты всех сотрудников за месяц — суммируем все числа.
    salaries = list(map(float, sys.stdin.read().split()))
    print(sum(salaries))


if __name__ == "__main__":
    main()
