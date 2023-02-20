nums=[]
print("Only 4 elements allowed")
for i in range(4):
    n=int(input("Enter element :"))
    nums.append(n)
midpoint=len(nums)//2
left=nums[:midpoint]
right=nums[midpoint:]
c=list((str(left[1])* (left[0])))
d=list((str(right[1])* (right[0])))
print((list(map(int,c)))+ (list(map(int,d))))