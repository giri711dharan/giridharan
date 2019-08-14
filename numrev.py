g=int(input(""))
r=0
while(g>0):
    dig=g%10
    r=r*10+dig
    g=g//10
print(r)
