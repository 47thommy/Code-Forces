def hx(arr1, arr2):
    w1 = w2 = w3 = 0
    ans = []
    for i in range(len(arr1)):
        res = w1 + w2*arr1[i] + w3*arr2[i]
        ans.append(res)
    
    return ans

def hx_score(hx, score):
    ans = []
    for i in range(len(hx)):
        res = hx[i] - score[i]
        ans.append(res)

    return ans

def hx_score_hx(hx_score, arr1):
    ans = []
    for i in range(len(hx_score)):
        res = hx_score[i] * arr1[i]
        ans.append(res)

    return ans


arr1 = [40,30,20,0,10]
arr2 = [110,120,100,90,80]
score = [100,90,80,70,60]


res_hx = hx(arr1, arr2)
print("hx()", res_hx)

res_hx_score = hx_score(res_hx, score)
print("hx() - score", res_hx_score)


res_hx_score_hx1 = hx_score_hx(res_hx_score, arr1)
res_hx_score_hx2 = hx_score_hx(res_hx_score, arr2)
print("hx() - score", res_hx_score)
print("hx() - score * arr1", res_hx_score_hx1)
print("hx() - score * arr2", res_hx_score_hx2)

def next_par(lr, w0, w1, w2):
    new0 = w0 - (lr * w0)
    new1 = w1 - (lr * w1)
    new2 = w2 - (lr * w2)
    
    return (new0, new1, new2)

w0 = sum(res_hx_score) / len(arr1)
w1 = sum(res_hx_score_hx1) / len(arr1)
w2 = sum(res_hx_score_hx2) / len(arr1)

print("sum1/m, sum2/m, sum3/m", w0, w1, w2)

print("next parameters")
w0, w1, w2 = next_par(1, w0, w1, w2)
print(w0, w1, w2)


