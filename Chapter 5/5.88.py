s=int(input());cnt=0
for i in range(100,1000):
 if sum(int(c) for c in str(i))==s:
  cnt+=1
print(cnt)
