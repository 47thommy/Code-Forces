n = int(input())
for _ in range(n):

  m = int(input())
  s = input()

  l = 0
  r = len(s) - 1

  while l < r and s[l] != s[r]:
    l += 1
    r -= 1
  
  if r > l :
    print(r-l + 1)
  
  else:
    if len(s)%2 == 0:
      print(0)
    else:
      print(1)