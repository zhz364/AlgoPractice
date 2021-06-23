## Day 2 06/23/21
## Question: Number of Occurrence:
#            you are given a sorted arr of numbers, and a target number as inputs, to write a function to determine how many time of the target number appers 
#            from the arr.
arr = [1]
    # =0,1,2,3,4,5,6,7
target = 7

def search(arr,target,l):
    ans = -1
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            if l:
                if arr[mid-1] != target:
                    return mid
                right = mid -1
                ans = mid
            else:
                if mid + 1 == len(arr) or arr[mid+1] != target:
                    return mid
                left = mid + 1
                ans = mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

# def searchRight(arr,target):
#     ans = -1
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         mid = (right + left) // 2
#         if arr[mid] == target:
#             if mid + 1 == len(arr) or arr[mid+1] != target:
#                 return mid
#             left = mid + 1
#             ans = mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return ans

def numberOfOccurrence(arr,target):
    left = search(arr,target,True)
    right = search(arr,target,False)

    if left == -1:
        return 0
    return right - left + 1


left = 0
right = 0
mid = 1
ans = 1

print(numberOfOccurrence(arr,target))


## things I learned:    

## 1. sorted arr means every occurrence of a number is together

## 2. binary search can help me find target and index 

## 3. if time complexity is log(n) DON'T EVEN THINK OF ITERATION

## 4. binary search needs to return a thing to break out the loop

## 5. mid need to update at the begining of a iteration, by adding index left and right then // 2

## 6. for this question, a helper function makes code clear, and by putting an extra input(in here is a boolean), can check both left and right in the same helper function. 
##    so don't need to write two helper functions for left and right check