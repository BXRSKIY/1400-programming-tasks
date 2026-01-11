import sys
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def main():
    a,b,c=map(int, sys.stdin.read().split()[:3])
    print(gcd(gcd(a,b),c))
if __name__=="__main__":
    main()
