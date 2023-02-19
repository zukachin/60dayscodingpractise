#Difference Between Element Sum and Digit Sum of an Array
nums=int(input("Enter the total no of elements: "))
l=[]
k=[]
for i in range(nums):
    m=int(input("Enter the elements: "))
    k.append(m)
    for j in str(m):
        l.append(j)
print(sum(list(map(int,k)))-sum(list(map(int,l))))

