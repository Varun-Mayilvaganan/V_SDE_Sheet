def max_min(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1,len(arr)-1):
        if arr[i] < arr[i+1]:
            min_val = min(min_val, arr[i])
        else:
            max_val = max(max_val, arr[i])
    return min_val, max_val
arr = [3, 1, 7, 9, 2, 5]   
print(max_min(arr))
