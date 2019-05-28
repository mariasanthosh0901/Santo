a1,b1=map(int,input().split())
l=[]
for i in range(a1+1,b1):
       if(i%2==0):
              l.append(i)
for i in l:
       print(i,end=' ')
              
