t = int(input())
for _ in range(t):
  count = 0
  n = int(input())
  array = list(map(int,input().split()))
  cache = [0] * n
  cache[n - 1] = array[n - 1]
  for i in range(n - 2,-1,-1):
    cache[i] = min(cache[i + 1],array[i])

  for i in range(n):
    if cache[i] < array[i]:
      count += 1
    
  print(count)

