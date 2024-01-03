n=int(input())
for _ in range(n):
  word=input()
  middle=word[1:len(word)-1]
  if len(word)<=10:
    res=word
  else:
    res=word[0]+str(len(middle))+word[len(word)-1]
  print(res)