# #if activity sorted by finish time
# def selection_sort(start,end):
#     ans = 0
#     finish = -1
#     for i in range(len(start)):
#         if(start[i] > finish):
#             finish = end[i]
#             ans += 1
#     return ans


# start = [1, 3, 0, 5, 8, 5]
# end = [2, 4, 6, 7, 9, 9]
# print(selection_sort(start,end))


def activity_sort(arr):
    ans = 0
    finish = -1

    arr.sort(key=lambda x: x[1])

    for i in arr:
        if(i[0] > finish):
            finish = i[1]
            ans += 1
    return ans



arr = [(3, 4), (0, 6), (5, 7), (8, 9), (5, 9), (1, 2)]
print(activity_sort(arr))