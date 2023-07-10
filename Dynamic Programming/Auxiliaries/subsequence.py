# using approach of pick and non-pick
def subsq(arr, temp, ptr):
    if ptr == len(arr):
        print(temp)
        return
    
    subsq(arr, temp, ptr+1)
    temp.append(arr[ptr])
    subsq(arr,temp, ptr+1 )
    temp.pop()

arr = [3, 2, 1]
temp = []
subsq(arr, temp, 0)