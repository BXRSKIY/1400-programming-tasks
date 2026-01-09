# 12.60. Дано предложение. Определить долю (в %) букв 'а' в нем.
s = input().rstrip("\n")
total = len(s)
pct = (s.count("а") / total * 100) if total else 0.0
print(f"{pct:.2f}")
