t=int(input())
for _ in range(t):
  b=input()
  ans=""
  for i in range(len(b)-2):
    if i %2==0:
      ans+=b[i]
  ans+=b[len(b)-2:]
  print(ans)



  