n,m = list(map(int, input().split()))
e=list(map(int,input().split()))
maximum=0
minimum=0
i=0

# while n >0:
#   e.sort()
#   maximum+=e[-1]
#   if e[-1]>0:
#     e[-1]-=1
#   n-=1
while n >0:
  e.sort()
  minimum+=e[i]
  n-=1
  e[i]-=1
  while e[i]>0:
    e[i]-=1
  i+=1


print(maximum)
print(minimum)
