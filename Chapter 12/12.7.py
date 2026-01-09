# 12.7. Даны две фамилии. Определить, какая длиннее (если равны — вывести "равны").
a = input().rstrip("\n")
b = input().rstrip("\n")
if len(a) > len(b):
    print(a)
elif len(b) > len(a):
    print(b)
else:
    print("равны")
