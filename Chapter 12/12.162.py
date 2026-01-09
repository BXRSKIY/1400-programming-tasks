s=input().replace(',','.');a,b=(s.split('.',1)+[''])[:2]
a=a.lstrip('+-').lstrip('0') or '0'
b=''.join(c for c in b if c.isdigit())
print(len(a));print(len(b))