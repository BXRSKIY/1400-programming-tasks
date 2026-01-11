import sys
def is_pal(s):
    return s==s[::-1]
def main():
    w=sys.stdin.read().split()
    if len(w)<3:
        return
    print("YES" if any(is_pal(x) for x in w[:3]) else "NO")
if __name__=="__main__":
    main()
