## Day 4 06/25/21

## Question:
##          verify alien dictionary: you are given an array of string called words and a string called order, return a boolean if the words are sorted
##          len(order) is always be 26, and len(words) >= 2.

words = ["ahelloag","ahelloag","h"]

order="hlabcdefgijkmnopqrstuvwxyz"

def is_alien_sorted(words, order):
    dic = {}
    for i in range(len(order)):
        dic[order[i]] = i
    for i in range(1,len(words)):
        length = min(len(words[i-1]),len(words[i]))
        for j in range(length):
            if dic[words[i-1][j]] < dic[words[i][j]]:
                break
            elif dic[words[i-1][j]] > dic[words[i][j]]:
                return False
            if j + 1 == len(words[i]) and len(words[i-1]) != len(words[i]):
                return False
    return True

print(is_alien_sorted(words, order))

## Things I learned:

## 1. For sorting, always done two each thing at a time, DO NOT TRY TO COMPARE ALL TOGETHER AT THE SAME TIME.
## 2. It's dumm to use a boolean for checking in the most of times, there should has a better way to check.
## 3. Sometings, when you have mutible if steatements, the checking order maybe matter. For this question, if put line 21 before line17, it will be cost an error 
##    when case ["hla","z"], it will skip rest of cases and return false at begenning of the iteration which's not true.
## 4. To counts the time and space compacities, if you know there's a constance number of cases, it will be O(1). Like the space for this one, I know the order string will always 
##    be 26 long, so the space is O(1).