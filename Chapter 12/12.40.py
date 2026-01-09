# 12.40. Напечатать заданное слово, начиная с последней буквы.
s = input().rstrip("\n")
for ch in reversed(s):
    print(ch, end="")
print()
