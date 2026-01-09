# 12.71. Слова разделены одним пробелом ('-' отсутствует). Верно ли, что число слов > 3?
s = input().rstrip("\n")
words = s.split(" ") if s else []
print("да" if len(words) > 3 else "нет")
