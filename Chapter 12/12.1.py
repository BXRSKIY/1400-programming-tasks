# 12.1. Ввести имя и фамилию (отдельно) и вывести как одну строку.
name = input().rstrip("\n")
surname = input().rstrip("\n")
print(f"{name} {surname}")
