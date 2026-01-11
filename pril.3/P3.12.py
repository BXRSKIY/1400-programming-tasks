x=1
y=-1
print(x**2 - y**2 <= 0)
x=2; y=-2
print((x>=2) or (y**2 != 4))
x=2; y=2
print((x>=0) and (y**2 > 4))
x=1; y=2
print((x*y != 4) and (y > x))
x=2; y=1
print((x*y != 0) or (y < x))
x=1; y=2
print((not (x*y < 1)) and (y > x))
x=2; y=1
print((not (x*y < 0)) or (y > x))
