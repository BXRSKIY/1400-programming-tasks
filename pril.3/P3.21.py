import itertools
def b(x):
    return 1 if x else 0
vars_=['A', 'B', 'C']
exprs=[('a', 'not (A or ((not B) and C))'), ('b', 'A and (not (B or (not C)))'), ('c', 'not (((not A) or B) and C)')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
