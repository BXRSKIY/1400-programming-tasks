# 12.144. Дано слово. Переставить его s-ю букву на место k-й (s > k).
# При этом k-я..(s-1)-я буквы сдвигаются вправо на 1.
word = input().rstrip("\n")
s, k = map(int, input().split())
s -= 1; k -= 1
lst = list(word)
ch = lst.pop(s)
lst.insert(k, ch)
print("".join(lst))
