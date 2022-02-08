def total(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+total(arr[1:])
