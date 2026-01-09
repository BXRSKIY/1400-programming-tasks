# 12.96. Дана строка, в которой есть слово "или". Определить, сколько раз оно встречается.
# Считаем "или" как отдельное слово.
s = input().rstrip("\n").lower()
matches = re.findall(r"(?<!\w)или(?!\w)", s, flags=re.UNICODE)
print(len(matches))
