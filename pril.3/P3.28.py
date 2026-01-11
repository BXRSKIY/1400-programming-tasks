exprs=['A>100 and B>100', '(A%2==0) ^ (B%2==0)', 'A>0 or B>0', 'A%3==0 and B%3==0 and C%3==0', '((A<50)+(B<50)+(C<50))==1', 'A<0 or B<0 or C<0']
print(*exprs, sep='\n')
