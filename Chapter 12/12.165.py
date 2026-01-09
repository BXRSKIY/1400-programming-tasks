s=input();
best=cur=1 if s else 0
for i in range(1,len(s)):
    if s[i]==s[i-1]: cur+=1; best=max(best,cur)
    else: cur=1
print(best)