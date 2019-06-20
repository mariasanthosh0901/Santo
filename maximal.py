n=input()
s=list(set(n))
count=0
for i in n:
    if i in s:
        count+=1
        s.remove(i)
    else:
        count+=1
        continue
    if(len(s)!=0):
        continue
    else:
        break
print(count)
