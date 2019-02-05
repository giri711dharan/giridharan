a=int(input("num:"))
b=int(input("num:"))
c=int(input("num:"))
if(a>b):
  if(a>c):
    print(a)
elif(b>c):
  print(b)
elif(c>a)and(c>b):
  print(c)
else:
  print(0)  
  
