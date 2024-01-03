n = int(input())

ans=0
for j in range(n):
  p=list(input().split())
  res=0
  for i in range(3):
    if(p[i]=="1"):
      res+=1
  if res>=2:
    ans+=1
print(ans)


