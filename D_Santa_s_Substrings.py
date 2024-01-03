n=int(input())
s=[]
for _ in range(n):
  s.append(input())
s.sort(key= lambda x : len(x))
for i in range(len(s)-1):
  if s[i] not in s[i+1] and s[i+1] not in s[i]:
    print("NO")
    exit()
  if len(s[i])==len(s[i+1]):
    if s[i] not in s[i+1]:
      s[i],s[i+1]=s[i+1],s[i]
print("YES")
for string in s:
  print(string)