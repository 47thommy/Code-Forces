
t = int(input())
for _ in range(t):

  n,k,q = [int(i) for i in input().split()]

  l = [int(i) for i in input().split()]

  count = 0
  ans = 0
  for ele in l:
    if ele <= q:
      count += 1
      if count >= k:
        ans += count - k + 1
    else:
      count = 0

  print(ans)



