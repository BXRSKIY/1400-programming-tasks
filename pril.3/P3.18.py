import itertools
def b(x):
    return 1 if x else 0
vars_=['X', 'Y']
exprs=[('a', '(not (X and (not Y))) or X'), ('b', '(Y and (not X)) or (not Y)'), ('c', '((not Y) and (not X)) or Y')]
print(' '.join(vars_+[n for n,_ in exprs]))
for values in itertools.product([False,True], repeat=len(vars_)):
    env=dict(zip(vars_, values))
    row=[b(env[v]) for v in vars_]
    for _,ex in exprs:
        row.append(b(eval(ex, {}, env)))
    print(' '.join(map(str,row)))
