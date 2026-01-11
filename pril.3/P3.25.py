import itertools
def b(x):
    return 1 if x else 0
vars_=['A', 'B', 'C']
exprs=[('a', 'not (A and B) and ((not A) or (not C))'), ('b', 'not (A and (not B)) or (A or (not C))'), ('c', '(A and (not B)) or (not (A or (not C)))')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
