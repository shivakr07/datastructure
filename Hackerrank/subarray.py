# def print_subarray(arr, st, end):
#     if end == len(arr):
#         return
#     elif st > end:
#         return print_subarray(arr, 0, end)
#     else:
#         print(arr[st : end+1])
#         return print_subarray(arr, st+1, end)
# Python3 code to print all possible subarrays
# for given array using recursion

# Recursive function to print all possible subarrays
# for given array
def printsubarray(arr, st, end):

	if end == len(arr):
		return

	elif st > end:
		return printsubarray(arr, 0, end + 1)

	else:
		print(arr[st:end + 1])
		return printsubarray(arr, st + 1, end)
		
# Driver code

arr = [2,-1,2,3,4,-5]
printsubarray(arr,0,0)


# ---------------------------------------------------
def maxSubarray(arr):
    # Write your code here
    def sumofsubarr(arr, st, end, ans1):
        if end == len(arr):
            return
        elif st > end:
            return sumofsubarr(arr, 0, end+1, ans1)
        else:
            ans1.append(sum(arr[st:end+1]))
            return sumofsubarr(arr, st+1, end, ans1)
    ans1 = []
    sumofsubarr(arr, 0, 0, ans1)
    ans2 = 0
    for i in arr:
        if i >= 0:
            ans2 += 1
    print(max(ans1), ans2)
    return max(ans1), ans2
ans1, ans2 = maxSubarray(arr)
print(ans1, ans2)


