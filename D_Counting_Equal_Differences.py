from collections import defaultdict
t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  count=0
  for i in range(n):
    for j in range(i,n):
      if i<j and a[j]-a[i]==j-i:
        count+=1
  print(count)