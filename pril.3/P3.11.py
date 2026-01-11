x=1
y=-1
print(x**2 + y**2 <= 4)
x=1; y=2
print((x>=0) or (y**2 != 4))
print((x>=0) and (y**2 != 4))
x=2; y=1
print((x*y != 0) and (y > x))
print((x*y != 0) or (y < x))
print((not (x*y < 0)) and (y > x))
x=1; y=2
print((not (x*y < 0)) or (y > x))
