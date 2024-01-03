t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int, input().split()))
  flag=False
  check=[]
  for i in range(n):
    for j in range(i+2,n):
      if a[i]==a[j]:
        flag=True
  if flag:
    print("YES")
  else:
    print("NO")


