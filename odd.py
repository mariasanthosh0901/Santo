a,b=map(int,input().split())
l=[]
for i in range(a+1,b+1):
       if(i%2!=0):
              l.append(i)
for i in l:
       print(i,end=' ')
              
              
