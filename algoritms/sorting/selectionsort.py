# a = [4,3,2,1]
# # print(a[a.index(4)+1:])
# for i in a:
#     small = min(a[(a.index(i)+1):])
#     if i > small:
#         temp = small
#         a[a.index(small)] = i
#         a[a.index(i)] = temp
# print(a)
arr = [3,1,4,2,5]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx = j

    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp
print(arr)