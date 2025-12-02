from math import gcd

def main():
    fracs = []
    for q in range(1, 8):
        for p in range(1, q):
            if gcd(p, q) == 1:
                fracs.append((p, q, p / q))
    fracs.sort(key=lambda t: t[2])
    for p, q, _ in fracs:
        print(f"{p}/{q}")


if __name__ == "__main__":
    main()
