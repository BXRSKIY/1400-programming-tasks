# 12.47. Дано слово. Добавить в начале и конце столько '*', сколько букв в слове.
s = input().rstrip("\n")
stars = "*" * len(s)
print(stars + s + stars)
