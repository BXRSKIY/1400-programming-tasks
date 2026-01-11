exprs=[
"(a==c) or (b==d)",
"abs(a-c)==abs(b-d)",
"max(abs(a-c),abs(b-d))==1",
"(a==c) or (b==d) or (abs(a-c)==abs(b-d))",
"(abs(a-c)==1 and d==b+1) or (a==c and d==b+1)",
"(abs(a-c)==1 and d==b-1) or (a==c and d==b-1)",
"sorted([abs(a-c),abs(b-d)])==[1,2]"
]
print(*exprs, sep='\n')
