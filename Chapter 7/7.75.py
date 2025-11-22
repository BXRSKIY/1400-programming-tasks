import math

def main():
    import sys
    # Траектория снаряда:
    # x(t) = v0 * cos(a) * t
    # y(t) = v0 * sin(a) * t - g * t^2 / 2
    # g = 9.8 м/с^2.
    # Формат ввода:
    # n, R, H, P, затем n пар: a, v0.
    # Угол a считаем заданным в радианах.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 4:
        raise ValueError("Ожидаются n, R, H, P и пары (a, v0)")
    n = int(data[0])
    R = data[1]
    H = data[2]
    P = data[3]
    expected_len = 4 + 2*n
    if len(data) < expected_len:
        raise ValueError(f"Ожидается {n} пар (a, v0)")
    g = 9.8
    hits = 0
    idx = 4
    for _ in range(n):
        a = data[idx]
        v0 = data[idx+1]
        idx += 2
        vx = v0 * math.cos(a)
        vy = v0 * math.sin(a)
        if vx == 0:
            continue
        t = R / vx
        if t < 0:
            continue
        y = vy * t - g * t * t / 2.0
        if H <= y <= H + P:
            hits += 1
    if n == 0:
        print(0.0)
    else:
        percent = hits * 100.0 / n
        print(percent)


if __name__ == "__main__":
    main()
