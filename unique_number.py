def find_uniq(arr):
    newlist = []
    for i in arr:
        if arr.count(i) == 1:
            print(i)


arr = [ 1, 1, 1, 2, 1, 1 ]
find_uniq(arr)