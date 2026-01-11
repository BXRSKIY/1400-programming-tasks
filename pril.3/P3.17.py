import itertools
def b(x):
    return 1 if x else 0
vars_=['A', 'B']
exprs=[('a', '((not A) and (not B)) or A'), ('b', 'B or ((not A) and (not B))'), ('c', 'B and (not (A and (not B)))')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
