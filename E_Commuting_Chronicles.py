n,m=map(int,input().split())

road=[]
check={}
for _ in range(n):
  road.append(list(input()))
for i in range(len(road)):
  for j in range(len(road[0])):
    if road[i][j]=="S":
      check["S"]=[i,j]
    if road[i][j]=="T":
      check["T"]=[i,j]
if (check["S"][0]==check["T"][0]):
  if check["S"][1]<check
  for j in range(len(road)):
    if road[check["S"][0]][j]:
