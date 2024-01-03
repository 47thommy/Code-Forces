

  for i in range(len(left)+len(right)):
    if(left[l]<right[r]):
      result.append(left[i])
      i+=1
    else:
      result.append(right[r])
      r+=1