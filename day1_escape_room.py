## Day 1 06/22/21
## Question:
##          You went into an escape room,there's N doors inside of the room. Each door has a keypad and you have a keyword dic. You need to write a function to determine
# how many solutions for each keypad. In additional, the first char in each keypad has to be in the keyword.   

words = ['apple', 'pleas', 'please']

keypads = [
    'aelwxyz',
    'aelpxyz',
    'aelpsxy',
    'saelprt',
    'xaebksy'  
]

ans = [0,1,3,2,0]

def escape_room(words,keypads):
    wordsBank = []
    ans = []
    for word in words:
        temp = set(word)
        wordsBank.append(temp)
    
    for keypad in keypads:
        temp = {}
        count = 0
        temp = set(keypad)
        for word in wordsBank:
            if keypad[0] in word and temp.issuperset(word):
                count += 1
        ans.append(count)
    
    return ans

print(escape_room(words,keypads))

## thing I learned:
## 1. Cannnot using "in" to compare with 2 dics, should use A.issubset(B) or B.issuperset(A) with two set which set B is including A