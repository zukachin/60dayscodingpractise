#Decompress run-length encoded list
nums=[1,2,3,4,5,6]
l=[]
for i in range(0,len(nums),2):
    a=nums[i]
    b=nums[i+1]
    l=l+[b]*a
print(l)

