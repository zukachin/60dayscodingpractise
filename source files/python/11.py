sentences=["alice and bob love leetcode","i think so too","this is great thanks very much "]
o=[]
for i in sentences:
    h=i.count(" ")+1
    o.append(h)
print(max(o))  

    

        