# 12.138. Дано слово. Переставить его s-ю букву на место k-й (s < k).
# При этом (s+1)..k буквы сдвигаются влево на одну позицию.
word = input().rstrip("\n")
s, k = map(int, input().split())
s -= 1; k -= 1
lst = list(word)
ch = lst.pop(s)
lst.insert(k, ch)
print("".join(lst))
