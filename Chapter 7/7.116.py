def main():
    import sys
    # Формат: ncars, nmotos, затем ncars цен автомобилей, затем nmotos цен мотоциклов.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются ncars и nmotos")
    nc, nm = int(data[0]), int(data[1])
    if len(data) < 2 + nc + nm:
        raise ValueError("Недостаточно данных о ценах")
    cars = data[2:2+nc]
    motos = data[2+nc:2+nc+nm]
    if not cars or not motos:
        print("NO")
        return
    avg_cars = sum(cars) / len(cars)
    max_moto = max(motos)
    cond = avg_cars > 5000 and avg_cars > max_moto
    print("YES" if cond else "NO")


if __name__ == "__main__":
    main()
