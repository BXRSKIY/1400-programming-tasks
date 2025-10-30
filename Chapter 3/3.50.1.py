h=int(input());m=int(input());t=0
while True:
 ah=(h%12)*30+m*0.5
 am=m*6
 if (abs(ah-am)%360)<1e-9:
  print(t);break
 m=(m+1)%60
 if m==0:
  h=(h%12)+1
 t+=1