from collections import defaultdict
n=int(input())
check=set()
numbers=defaultdict(list)
for i in range(n):
  name=input()
  if name in check:
    num=numbers[name][-1]+1
    check.add(name+str(num))
    numbers[name].append(num)
    print(name+str(num))
  else:
    check.add(name)
    numbers[name].append(0)
    print("OK")