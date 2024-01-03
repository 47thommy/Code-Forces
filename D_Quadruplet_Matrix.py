t=int(input())
for _ in range(t):
  count=0
  count2=0
  board=[]
  n=int(input())
  for _ in range(n):
    board.append(list(input()))
t,b=n-0,n-1
while t<=b:
  if board[t][0] == "0":
    count+=1
  if board[t][b-t]=="0":
    count+=1