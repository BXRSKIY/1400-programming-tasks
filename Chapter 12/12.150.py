# 12.150. Дан текст, в котором имеются цифры:
# a) найти их сумму;
# б) найти максимальную цифру.
s = input().rstrip("\n")
digits = [int(ch) for ch in s if ch.isdigit()]
print(sum(digits))
print(max(digits))
