s=0
for i in range(31,100):
 if i%3==0 and i%10 in [2,4,8]:
  s+=i
print(s)
