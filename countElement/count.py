def countElements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1+countElements(arr[1:])