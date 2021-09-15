def rearrange(arr) :
    j = 0
    for i in range(len(arr)) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    return arr