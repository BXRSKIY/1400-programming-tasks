s=input().replace('–','-');d=[];op=[]
for c in s:
    if c.isdigit(): d.append(int(c))
    elif c in '+-': op.append(c)
r=d[0]
for o,x in zip(op,d[1:]): r=r+x if o=='+' else r-x
print(r)