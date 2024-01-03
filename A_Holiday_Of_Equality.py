n=int(input())
w=list(map(int,input().split()))
w.sort()

ans=0
m=w[-1]
for i in range(len(w)):
  ans+=m-w[i]
print(ans)
