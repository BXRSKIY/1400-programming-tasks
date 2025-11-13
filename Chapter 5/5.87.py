cnt=0
for i in range(100,501):
 if sum(int(c) for c in str(i))==15:
  cnt+=1
print(cnt)
