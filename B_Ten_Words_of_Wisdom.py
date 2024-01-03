
t = int(input())

for _ in range(t):
    n = int(input()) 
    responses = []

    for i in range(n):
        a, b = map(int, input().split())
        responses.append((a, b, i + 1))  

   
    responses.sort(key=lambda x: (-x[1], x[0]))

    winner = None
    for response in responses:
        if response[0] <= 10:
            winner = response[2]
            break

    print(winner)
