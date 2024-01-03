t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  pivot=-1
  for i in range(n-1):
    temp=-1
    if a[i]<a[i+1]:
      temp=0
    if a[i]>a[i+1]:
      temp=(a[i]+a[i+1])//2
    if abs( a[i]-pivot)>abs(a[i+1]-pivot):
      pivot=-1
    pivot=max(pivot,temp)
  print(pivot)

    

