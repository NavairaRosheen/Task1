num=input("Enter Number : ")
mul=1
sum=0
i=0
while i<3:
    sum=int(num)*mul+sum
    mul=mul*int(num)
    i+=1
print(sum)