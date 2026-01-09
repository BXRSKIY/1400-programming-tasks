# 12.186. Напечатать все слова предложения в порядке неубывания их длин.
s = input().rstrip("\n")
words = s.split()
words.sort(key=len)
print(" ".join(words))
