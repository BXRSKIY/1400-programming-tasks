s=input().split(' ');
print(' '.join(x for x in s if x and x[0]==x[-1]));print(' '.join(x for x in s if x.count('е')==3));print(' '.join(x for x in s if 'о' in x))