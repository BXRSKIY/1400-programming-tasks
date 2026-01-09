# 12.147. Дан символ. Выяснить, является ли он цифрой.
s = input().rstrip("\n")
ch = s[0] if s else ""
print("да" if ch.isdigit() else "нет")
