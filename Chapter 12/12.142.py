# 12.142. Дано слово. Переставить его последнюю букву на место k-й.
# При этом k-я..предпоследняя буквы сдвигаются вправо на 1.
word = input().rstrip("\n")
k = int(input()) - 1
if not word or k < 0 or k >= len(word):
    print(word)
else:
    last = word[-1]
    lst = list(word[:-1])
    lst.insert(k, last)
    print("".join(lst))
