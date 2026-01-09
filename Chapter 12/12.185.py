# 12.185. Верно ли, что самое длинное слово предложения имеет больше 10 символов?
s = input().rstrip("\n")
words = s.split()
print("да" if max(len(w) for w in words) > 10 else "нет")
