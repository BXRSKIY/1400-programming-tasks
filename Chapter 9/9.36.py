def main():
    # Найти размеры всех прямоугольников с площадью s (натуральные стороны).
    # а) решения, отличающиеся перестановкой сторон, считать разными;
    # б) совпадающими.
    s = int(input())
    # а) все упорядоченные пары (a,b)
    print("variant_a")
    for a in range(1, s + 1):
        if s % a == 0:
            b = s // a
            print(a, b)
            if a != b:
                print(b, a)
    # б) только пары с a <= b
    print("variant_b")
    for a in range(1, int(s ** 0.5) + 1):
        if s % a == 0:
            b = s // a
            if a <= b:
                print(a, b)


if __name__ == "__main__":
    main()
