nums=[int(input()) for _ in range(20)];p=1;f=False
for x in nums:
    if x>0:p*=x;f=True
print(p if f else 0)