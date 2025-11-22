def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 50:
        raise ValueError("Ожидается 25 пар (s, t)")
    max_speed = None
    idx_max = 0
    for i in range(25):
        s = data[2*i]
        t = data[2*i+1]
        if t == 0:
            continue
        v = s / t
        if max_speed is None or v > max_speed:
            max_speed = v
            idx_max = i + 1
    print(idx_max)


if __name__ == "__main__":
    main()
