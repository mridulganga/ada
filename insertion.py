def insertion(arr):
    for i in xrange(len(arr)):
        pos=i
        insert = arr[i]
        while(pos > 0 and arr[pos-1] > insert):
            arr[pos] = arr[pos-1]
            pos-=1
        arr[pos] = insert


a1 = [7,2,4,1,8,5]
insertion(a1)
print a1
