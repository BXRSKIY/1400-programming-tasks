import math
y=float(input());hours=int((y%(2*math.pi))/(math.pi/6));minutes=int(((y%(math.pi/6))/(math.pi/30)));print(hours,minutes)