def cross_max_arr(arr,low,mid,high):
    s = 0
    left_sum = float('-inf')
    for i in range(mid,low-1,-1):
        s = s + arr[i]
        left_sum = max(left_sum,s)

    s = 0
    right_sum = float('-inf')
    for i in range(mid+1,high+1):
        s = s + arr[i]
        right_sum = max(right_sum,s)

    return left_sum + right_sum

def max_sub_arr(arr,low,high):
    if(low==high):
        return arr[low]
    
    mid = (low+high) // 2
    left_max = max_sub_arr(arr,low,mid)
    right_max = max_sub_arr(arr,mid+1,high)
    cross_max = cross_max_arr(arr,low,mid,high)
    
    return max(left_max, right_max, cross_max)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_arr(arr,0,len(arr)-1))