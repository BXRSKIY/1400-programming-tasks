def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True
def main():
    for n in range(100,1000):
        if is_prime(n):
            print(n)
if __name__=="__main__":
    main()
