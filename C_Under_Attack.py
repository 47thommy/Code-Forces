t = int(input())
for _ in range(t):
  n,m=map(int,input().split())
  matrix=[]
  for _ in range(n):
    matrix.append(list(input().split()))
  maxSum=0
  i,j=0,0
  
  while i<n and j<m:
    maxSum+=matrix[i][j]
    i+=1
    j+=1


