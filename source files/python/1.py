# Number of Steps to Reduce a Number to Zero
num=int(input("Give a number: "))
i=0
while num!=0:
    if num%2==0:
        num/=2
        i+=1
    else:
        num-=1
        i+=1
print(i)

