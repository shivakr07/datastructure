def largestPermutation(arr,k):
    ptr = 0
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i
    while k > 0:
        m = max(arr[ptr:])
        i = d[m]
        arr[i],arr[ptr] = arr[ptr],arr[i]
        ptr += 1
        k -= 1
    return arr
arr = [2,3,5,1,4]
k = 3
ans = largestPermutation(arr, k)
print(ans)