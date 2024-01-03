p=list(input())
flag=False
for c in p:
  if c=="H" or c == "Q" or c=="9":
    flag=True
if flag:
  print("YES")
else:
  print("NO")
