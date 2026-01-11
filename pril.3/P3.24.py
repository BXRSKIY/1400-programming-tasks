import itertools
def b(x):
    return 1 if x else 0
vars_=['X', 'Y', 'Z']
exprs=[('a', 'not ((Y or ((not X) and Z))) or Z'), ('b', 'X and (not ((not Y) or Z)) or Y'), ('c', 'not ((X or (Y and Z))) or (not X)')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
