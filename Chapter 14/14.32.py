import sys
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def main():
    a,b=map(int, sys.stdin.read().split()[:2])
    g=gcd(a,b)
    print(a//g, b//g)
if __name__=="__main__":
    main()
