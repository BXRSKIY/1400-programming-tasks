import math
def f(n):
    return (n+math.sqrt(n))/(math.sqrt(n)+n)
def g(n):
    return (n+math.sqrt(n))/(n+math.sqrt(n))
def term(a,b):
    return (a+math.sqrt(a))/(math.sqrt(b)+b)
def main():
    a = (5+math.sqrt(5))/(math.sqrt(7)+7) + (12+math.sqrt(12))/(math.sqrt(8)+8) + (31+math.sqrt(31))/(math.sqrt(2)+2)
    b = (13+math.sqrt(7))/(7+math.sqrt(13)) + (15+math.sqrt(12))/(math.sqrt(15)+12) + (math.sqrt(21)+32)/(math.sqrt(32)+21)
    print(a)
    print(b)
if __name__=="__main__":
    main()
