n=int(input())
num=list(map(int,input().split()))
even=[]
odd=[]
total=0
if n==0:
  print(0)
  exit()
elif n==1 and num[0]%2!=0:
  print(0)
  exit()
for i in num:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
if len(odd)%2!=0:
  odd.sort()
  oddsum=sum(odd[1:len(odd)])
else:
  oddsum=sum(odd)
evensum=sum(even)
total=oddsum+evensum
print(total)
  