n=input()
max1=len(n)
w=len(n)
x=0
def val(x1,w,n,s,max1):
       count=0
       for i in range(x1,w):
              if n[i] in s:
                     count+=1
                     s.remove(n[i])
              else:
                     count+=1
                     continue
              if(len(s)!=0):
                     continue
              else:
                     break
       if(len(s)==0):
              return count
       else:
              return max1
for i in range(x,w):
       s=list(set(n))
       res=val(x,w,n,s,max1)
       if(res<max1):
              max1=res
              res=0
       x+=1
print(max1)
