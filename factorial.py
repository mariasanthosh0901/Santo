def fact(num):
       if(num>0 and num!=1):
              return num*fact(num-1)
       elif(num==1):
              return num
fac=int(input())
if(fac>0):
       print(fact(fac))
