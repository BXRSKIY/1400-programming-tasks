A=False
B=False
C=True
print(((not A) or (not B)) and (not C))
print(((not A) or (not B)) and (A or B))
print((A and B) or (A and C) or (not C))
