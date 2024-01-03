for _ in range(int(input())):
	n = int(input())
	s = input()
	c = {}
	for i in range(n - 1):
		t = s[i:i+2]
		if t in c:
			if c[t] < i - 1:
				print("YES")
				break
		else:
			c[t] = i
	else:
		print("NO")