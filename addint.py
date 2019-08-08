n,m=map(int,input().split())
sum=0
con = [int(i) for i in input().split()]
for i in range(0,m):
    sum+=con[i]
print(sum)
