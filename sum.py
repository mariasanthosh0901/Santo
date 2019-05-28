n,k=map(int,input().split())
sum=0
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(k):
    sum+=l[i]
print(sum)
