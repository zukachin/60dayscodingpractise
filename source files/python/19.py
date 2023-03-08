#prime number:
n=int(input("Enter the number: "))
if 6*n+1 and n%2!=0 or 6*n-1 and n%2!=0 or n==2 or n==3 : 
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")