area=100.0
yield_ha=20.0
year=1
y1=y2=y3=None
total=0.0
while True:
    total+=area*yield_ha
    if y1 is None and yield_ha>22:
        y1=year
    if y2 is None and area>120:
        y2=year
    if y3 is None and total>800:
        y3=year
    if y1 and y2 and y3:
        break
    year+=1
    area*=1.05
    yield_ha*=1.02
print(y1)
print(y2)
print(y3)
