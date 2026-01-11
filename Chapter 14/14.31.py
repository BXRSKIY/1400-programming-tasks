import sys, math
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a//gcd(a,b)*b
def main():
    a,b=map(int, sys.stdin.read().split()[:2])
    print(lcm(a,b))
if __name__=="__main__":
    main()
