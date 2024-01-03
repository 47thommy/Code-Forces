from collections import Counter
t=int(input())
for _ in range(t):
  n=int(input())
  nums=list(input().split())
  count=Counter(nums)
  for key in count:
    if count[key]==1:
      print(nums.index(key)+1)