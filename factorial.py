def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
s=int(input("Enter a number:"))
print(fact(s))    


#**************************************************************************
#second method
num=int(input("Enter a number:"))
if num<0:
    print("0")
elif num==0 or num==1:
    print("1")
else:
    fact =1
    while num>0:
        fact = fact*num
        num=num-1
    print(fact)            