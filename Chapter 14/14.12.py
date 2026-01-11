import math
def t(a,b):
    return (a+math.sin(a))/(math.sin(b)+b)
def main():
    y1 = (2+math.sin(2))/(math.sin(5)+5) + (6+math.sin(6))/(math.sin(3)+3) + (1+math.sin(1))/(math.sin(4)+4)
    y2 = (1+math.sin(4))/(4+math.sin(1)) + (7+math.sin(5))/(5+math.sin(7)) + (3+math.sin(2))/(2+math.sin(3))
    print(y1)
    print(y2)
if __name__=="__main__":
    main()
