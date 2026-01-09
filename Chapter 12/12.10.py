# 12.10. Обмен значениями трех строк a, b, c по схеме:
# a) b := c, a := b, c := a (то есть циклический сдвиг влево: a<-b<-c<-a)
# б) b := a, c := b, a := c (циклический сдвиг вправо: a<-c<-b<-a)
#
# Ввод: строка a, строка b, строка c, затем символ 'a' или 'b' (вариант).
a = input().rstrip("\n")
b = input().rstrip("\n")
c = input().rstrip("\n")
variant = input().strip()

if variant.lower() == "a":
    # new_b = c; new_a = b; new_c = a
    a, b, c = b, c, a
elif variant.lower() == "b":
    # new_b = a; new_c = b; new_a = c
    a, b, c = c, a, b
else:
    raise SystemExit("Variant must be 'a' or 'b'")

print(a)
print(b)
print(c)
