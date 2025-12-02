import itertools

def main():
    # Прямоугольные параллелепипеды объёмом v, стороны — натуральные.
    # а) перестановку сторон считать разными;
    # б) совпадающими.
    v = int(input())
    triples_b = []
    # сначала найдём уникальные тройки a<=b<=c
    for a in range(1, v + 1):
        if a * a * a > v:
            break
        if v % a != 0:
            continue
        v1 = v // a
        for b in range(a, v1 + 1):
            if a * b * b > v:
                break
            if v1 % b != 0:
                continue
            c = v1 // b
            if c < b:
                continue
            triples_b.append((a, b, c))
    # б) печать уникальных троек
    print("variant_b")
    for a, b, c in triples_b:
        print(a, b, c)
    # а) печать всех перестановок
    print("variant_a")
    for a, b, c in triples_b:
        perms = set(itertools.permutations((a, b, c)))
        for p in perms:
            print(*p)


if __name__ == "__main__":
    main()
