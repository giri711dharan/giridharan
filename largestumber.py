a=int(input("num1:"))
b=int(input("num2:"))
c=int(input("num3:"))
if(a>b):
  if(a>c):
    print(a)
elif(b>c):
  print(b)
elif(c>a)and(c>b):
  print(c)
else:
  print(0)  
  
