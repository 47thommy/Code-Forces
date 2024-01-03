t = int(input())
for _ in range(t):
  run=list(map(int,input().split()))
  count=0
  for i in range(1,len(run)):
    if run[i]>run[0]:
      count+=1
  print(count)
    

