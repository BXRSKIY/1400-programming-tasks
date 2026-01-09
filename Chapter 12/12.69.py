# 12.69. Дано предложение. Какая из букв — 'о' или 'а' — встречается чаще (обе буквы есть).
s = input().rstrip("\n")
co = s.count("о")
ca = s.count("а")
print("о" if co > ca else ("а" if ca > co else "равно"))
