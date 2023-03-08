operation=['--x','x--','++x']
count=0
for i in operation:
    if i == "--x" or i=="x--":
            count+=-1
    elif i== "x++" or i=="++x":
           count+=1
print(count)
     

