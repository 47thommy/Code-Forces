t=int(input())
for _ in range(t):
  n,m=list(map(int,input().split(" ")))
  nums=list(map(int,input().split()))
  nums.sort()
  check=n+(sum(nums))-nums[0]+nums[-1]
  if check > m:
    print("NO")
  else:
    print("YES")
