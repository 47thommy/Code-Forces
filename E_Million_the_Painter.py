n=int(input())
c=list(input())
flag=True
check={}

if c.count("?")==0:
  flag=False
for i in range(n-1):
  if c[i]==c[i+1] and c[i]!="?":
    flag=False
if c[-1]!="?" and c[0]!="?":
  for k in range(n-1):
    if c[k]=="?":
      if c[k-1]!="?" and c[k+1]!="?":
        check[c[k-1]]=check.get(c[k-1],0)+1
        check[c[k+1]]=check.get(c[k+1],0)+1
if n == 1 and c[0]!="?":
  flag=False
if c.count("?")==1:
  for j in range(n-1):
    if c[j]=="?" and j!=0:
      if j!=n-1:
        if c[j-1]!=c[j+1]:
          flag=False

checky=sum(check.values())

if len(check)==2 and checky!=4:
  flag=False
if flag:
  print("Yes")
else:
  print("No")

