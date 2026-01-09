# 12.116. Устранить ошибку:
# a) "глинянный" -> "глиняный"
# б) "граффика" -> "графика"
# Ввод: вариант ('a' или 'b').
variant = input().strip().lower()
if variant == "a":
    print("глиняный")
elif variant == "b":
    print("графика")
else:
    raise SystemExit("Variant must be 'a' or 'b'")
