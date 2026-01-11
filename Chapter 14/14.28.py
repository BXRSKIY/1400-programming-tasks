def sum3(n):
    return n//100 + (n//10)%10 + n%10
def main():
    cnt_last=[0]*28
    for x in range(0,1000):
        cnt_last[sum3(x)]+=1
    cnt=0
    for first in range(100,1000):
        cnt += cnt_last[sum3(first)]
    print(cnt)
if __name__=="__main__":
    main()
