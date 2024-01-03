n,m = map(int,input().split())
p=list(map(int,input().split()))
temp=m
p.sort()
ans=0
if p[0] >=0:
  print(0)
else:
 for i in range(m):
   if p[i]<0:
     ans=ans+p[i]
     m-=1
print(0-(ans))
     
    