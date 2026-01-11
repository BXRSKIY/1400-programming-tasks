import sys
def is_pal(n):
    s=str(n)
    return s==s[::-1]
def main():
    a,b=map(int, sys.stdin.read().split()[:2])
    print("YES" if is_pal(a) or is_pal(b) else "NO")
if __name__=="__main__":
    main()
