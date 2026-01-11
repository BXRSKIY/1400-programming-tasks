def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True
def main():
    for p in range(2,199):
        if is_prime(p) and is_prime(p+2) and p+2<=200:
            print(p, p+2)
if __name__=="__main__":
    main()
