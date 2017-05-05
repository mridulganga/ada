def merge(arr,low,mid,high):
    L = [0]*(mid-low+1)
    R = [0]*(high-mid)

    for i in xrange(len(L)):
        L[i] = arr[low+i]
    for i in xrange(len(R)):
        R[i] = arr[mid+i+1]

    i=0
    j=0
    k=low
    result = []
    while( i<len(L) and j<len(R)):
        if (L[i]<=R[j]):
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while (i<len(L)):
        arr[k] = L[i]
        i+=1
        k+=1
    while (i<len(R)):
        arr[k] = R[i]
        i+=1
        k+=1


def mergesort(arr,low,high):
    if (low<high):
        mid = low + (high-low)/2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)


a1 = [6,2,3,9,1,4]
mergesort(a1,0,len(a1)-1)
print a1
