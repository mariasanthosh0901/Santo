a1,b1=map(int,input().split())
l=[]
for i in range(a1+1,b1):
       sum=0
       te=i
       while(i>0):
              dig=i%10
              sum+=dig**3
              i=i//10
       if(te==sum):
              l.append(te)
for i in l:
       print(i,end=' ')
              
              
              
