n=int(input())
m=n
s=0
while(n>0):
    dig=n%10
    s=s*10+dig
    n=n//10
if(s==m):
    print("yes")
else:
    print("no")
