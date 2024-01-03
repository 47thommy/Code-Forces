t=int(input())

for _ in range(t):
  n=input()
  nums=input().split()
  if len(nums)==len(set(nums)):
    print("YES")
  else:
    print("NO")