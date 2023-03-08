#fibonnaci
#0,1,1,2,3,5
n=int(input("Enter the no.of. elements to be shown: "))
f=[0,1]
for i in range(n-2):
    f.append(f[-1]+f[-2])
print(f)
    
