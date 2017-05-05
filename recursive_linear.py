def search(alist, key, pos=None):
    if pos is None: pos = len(alist) - 1
    if pos < 0: return None
    if key == alist[pos]: return pos
    return search(alist, key, pos - 1)

a = [2,1,5,7,8,9,13]
print search(a,5)
