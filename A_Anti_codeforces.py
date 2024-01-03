t=int(input())
c="codeforces"
for _ in range(t):
  s=input()
  count=0
  for i in range(10):
    if s[i]!=c[i]:
      count+=1
  print(count)



  