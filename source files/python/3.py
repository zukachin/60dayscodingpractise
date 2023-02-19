#sorting the sentences
sentence="is2 sentence4 This1 a3"
print(sentence)
g=(sentence.split(" "))                        
l=[]
e=[] 
final=[]
for kim in g:
    e.append((kim[-1]))
p=(sorted(e)) #1,2,3,4
h=list(g)
for item in p:
    for item2 in h:
        if item==item2[-1]:
            l.append(item2)   
for jk in l:
     v= jk[:-1]
     final.append(v)
print(" ".join(final))