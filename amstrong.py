num = int(input())
temp = num
sum = 0
length = len(str(num))
while num != 0:
    rem = num % 10
    sum = sum +rem ** length
    num = num // 10
if temp == sum:
    print("Amstrong")
else:
    print("Not Amstrong")        