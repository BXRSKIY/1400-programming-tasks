# 12.63. Дано предложение. Определить:
# a) число вхождений буквосочетания "ро";
# б) число вхождений некоторого буквосочетания из двух букв;
# в) число вхождений некоторого буквосочетания (любой длины).
#
# Ввод:
# 1) строка s
# 2) строка p2 (две буквы) — для пункта (б)
# 3) строка p (любой длины) — для пункта (в)
s = input().rstrip("\n")
p2 = input().rstrip("\n")
p = input().rstrip("\n")

def count_overlapping(text, pat):
    if not pat:
        return 0
    c = 0
    for i in range(0, len(text) - len(pat) + 1):
        if text[i:i+len(pat)] == pat:
            c += 1
    return c

print(count_overlapping(s, "ро"))
print(count_overlapping(s, p2))
print(count_overlapping(s, p))
