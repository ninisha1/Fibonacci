n=int(input("enter the value"))
a=0
b=1
sum=0
count=0
print("fibonacci series:")
while count<n:
    print(sum)
    count+=1
    a=b
    b=sum
    sum=a+b
