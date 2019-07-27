import re
str1=input()
count=0
for i in str1:
       if re.match('[a-zA-Z]',i):
              count+=1
print(count)
