def binarys(arr,key,low,high):
    mid = (low+high)/2
    if (key==arr[mid]):
        return mid
    elif arr[mid] < key:
        return binarys(arr,key,mid+1,high)
    else:
        return binarys(arr,key,low,mid-1)


a1 = [2,4,5,7,8,9]
key = 5
print binarys(a1,key,0,len(a1)-1)
