# 12.36. Дано слово из 12 букв. Поменять местами его трети.
# Ввод: слово, затем вариант ('a' или 'b').
s = input().rstrip("\n")
variant = input().strip().lower()
third = len(s) // 3  # должно быть 4

a, b, c = s[:third], s[third:2*third], s[2*third:]
if variant == "a":
    # 1/3 -> на место 3-й, 2-я -> на место 1-й, 3-я -> на место 2-й
    print(b + c + a)
elif variant == "b":
    # 1-я -> на место 2-й, 2-я -> на место 3-й, 3-я -> на место 1-й
    print(c + a + b)
else:
    raise SystemExit("Variant must be 'a' or 'b'")
