a=input();b=input();c=input();v=input();
if v=='2':
    S=[set(a),set(b),set(c)];print(' '.join(sorted(x for x in S[0]|S[1]|S[2] if sum(x in s for s in S)==1)))
else:
    out=[];SB=set(b)|set(c)
    for x in a:
        if x not in SB: out.append(x)
    SA=set(a)|set(c)
    for x in b:
        if x not in SA: out.append(x)
    SC=set(a)|set(b)
    for x in c:
        if x not in SC: out.append(x)
    print(' '.join(out))