string=input('Enter using "G","()","(al)": ')
command={'G':'G','g':'G','()':'o','(al)':'al'}
for cha in command.keys():
    g=string.replace(cha,command[cha])
print(g.replace("()","o"))
