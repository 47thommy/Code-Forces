n = int(input())
for i in range(n):
    m = int(input())
    li = [int(j) for j in input().split()]
    li.append(float('inf'))
    valley = 0
    l,r = 0,0
    
    while r < len(li):
        if li[r] == li[l]:
            r += 1
        elif li[r] > li[l]:
            if l-1 >=0 :
                if li[l-1] > li[l]:
                    valley += 1
                    l = r
                    r += 1
                else:
                    l = r
                    r += 1
            else:
                valley += 1
                l = r
                r += 1
        else:
            l = r
            r += 1
        
 
            
    if valley == 1:
        print("YES")
    else:
        print("NO")