def main():
    # Полная таблица умножения 1..9
    for y in range(1, 10):
        row = []
        for x in range(1, 10):
            row.append(f"{x}*{y}={x*y}")
        print(" ".join(row))


if __name__ == "__main__":
    main()
