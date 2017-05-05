def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in xrange(low,high):
        if (arr[j]<pivot):
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def qsort(arr,low,high):
    if (low<high):
        pi = partition(arr,low,high)
        qsort(arr,low,pi-1)
        qsort(arr,pi+1,high)

a1 = [5,2,7,3,9,1]
qsort(a1,0,len(a1)-1)
print a1
