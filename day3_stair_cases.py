## Day 3 06/24/21
## Question:
##          You are give a input n which is how many stairs you have, and wriete a function to determine how ways you can get to n stairs. You can 
#           only go 1 or 2 step at each time

## sounds like fib sequcence, but this is too slow O(2^n)
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    return num_ways(n-2) + num_ways(n-1)

## use space to reduce time: so time is O(n), and space also is O(n)
def num_ways_time(n):
    if n == 0 or n == 1:
        return 1
    count = [1,1]
    for i in range(2,n+1):
        temp = count[i-2] + count[i-1]
        count.append(temp)
    return count[-1]
## can be done better with space, realized only need 2 variables to save more space so now time is O(n) and space is O(1)
def num_ways_space(n):
    if n == 0 or n == 1:
        return 1
    prev1 = 1
    prev2 = 1
    for i in range(2,n+1):
        temp = prev2
        prev2 += prev1
        prev1 = temp
    return prev2

## Now question changed about steps, we are no longer go 1 or 2 at each time, we go different steps. So you will have an array of numbers, each number is 
## step you can go. You need to write a function to determine how many ways can get to the n stairs with different step from the arr.

## For the fib solution(num_ways()) we found out the trick is the current steps is by adding preves 2 steps. But for this one, we don't know how many steps we will have,
## but we do realized in somehow fib still works on this, but it's modified.
## So our base case only when n == 0 holds true, and since we don't know how many steps we have, so add all possible each step together
## the time is k^n where k is the len(steps)
def num_ways_steps(n,steps):
    if n == 0:
        return 1
    ans = 0
    for step in steps:
        if n - step >= 0:
            ans += num_ways_steps(n-step,steps)
    return ans


## Kind use the idea from num_ways_time solution, we found we can go similer way
def num_ways_steps_kn(n,steps):
    if n == 0:
        return 1
    count = [1]
    for i in range(1,n+1):
        temp = 0
        for step in steps:
            if i - step >= 0:
                temp += count[i-step]
        count.append(temp)
    return count[-1]

print(num_ways_steps_kn(5,[1,3,5]))

## Things I learned 
## 1. Write down more cases to looking for the trick
## 2. Use more space to reduce time, and sometime no really need to create a data sture, a variable maybe works too