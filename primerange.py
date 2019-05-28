a,b=map(int,input().split())
l=[]
for i in range(a+1,b+1):
       count=1
       for j in range(2,i):
              if(i%j==0):
                     count=0
       if(count==1):
              l.append(i)
for k in l:
       print(k,end=' ')
