nu = int(input())
sum = 0
temp = nu
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if nu == sum:
   print("yes")
else:
   print("no")
