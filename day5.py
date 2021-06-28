## Day 5 06/28/21

## Question: Given an array of intergers, return the index where the sum of all elements to the left is equal to the sum of all elements to the right.
# 
arr = [2,0]


def sumLeftandRight(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    left = 0
    for i in range(0,len(arr)):
        if i > 0:
            left += arr[i-1]
        right = 0
        for j in range(i+1,len(arr)):
            right += arr[j]
        if left == right:
            return i
    return -1        

def sumLeftandRight_faster(arr):
    left = 0
    right = sum(arr)
    for i in range(0,len(arr)):
        if i > 0:
            left += arr[i-1]
        right -= arr[i]
        if left == right:
            return i
    return -1   

print(sumLeftandRight_faster(arr))

## Things I learned:

## 1. For the solution 1, the time takes O(n^2) which is not fast. In general, rewriting the inner loop can reduce the time. so come up with other idea for it
## 2. For loop is best to start from index 0 to cover all satuiations. For example, I was started from index 1 so then case[2,0] (this should be return 0) got wrong return.
