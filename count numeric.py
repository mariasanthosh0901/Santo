import re
str1=input()
c=0
for i in str1:
       if re.match('[0-9]',i):
              c+=1
print(c)
       
