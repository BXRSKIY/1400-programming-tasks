# 12.9. Даны названия двух стран. Обменять значения s1 и s2.
s1 = input().rstrip("\n")
s2 = input().rstrip("\n")
s1, s2 = s2, s1
print(s1)
print(s2)
