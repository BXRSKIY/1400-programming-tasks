import itertools
def b(x):
    return 1 if x else 0
vars_=['X', 'Y', 'Z']
exprs=[('a', 'not (X or Y) and ((not X) or (not Z))'), ('b', 'not ((not X) and Y) or (X and (not Z))'), ('c', 'X or ((not Y) and (not (X or (not Z))))')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
