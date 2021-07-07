## Day 7 07/06/21
## Question: write a class for singly link list

class node:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class linkedList:
    def __init__(self,arr):
        self.root = None
        for i in range(len(arr)):
            if i == 0:
                self.root = node(arr[i])
                currNode = self.root
            else:
                currNode.next = node(arr[i])
                currNode = currNode.next
        
    def printVal(self):
        arrVal = []
        currNode = self.root
        while currNode:
            arrVal.append(currNode.val)
            currNode = currNode.next 
        print(arrVal)       
    
    def deleteNode(self,val):
        currNode = self.root
        prev = None
        while currNode:
            if currNode.val == val:
                if currNode == self.root:
                    currNode = currNode.next
                    self.root = currNode
                else:
                    prev.next = currNode.next
                    currNode = currNode.next
            else:
                prev = currNode
                currNode = currNode.next

            
# delete root node
arr = [4,3,1]
ll = linkedList(arr)
ll.printVal()
ll.deleteNode(4)
ll.printVal()

# delete node in middle
arr = [4,3,1]
ll = linkedList(arr)
ll.printVal()
ll.deleteNode(3)
ll.printVal()

# delete a non-existing node
arr = [4,3,1]
ll = linkedList(arr)
ll.printVal()
ll.deleteNode(5)
ll.printVal()

# delete all nodes
arr = [4,4,4]
ll = linkedList(arr)
ll.printVal()
ll.deleteNode(4)
ll.printVal()

# delete node from empty arr
arr = []
ll = linkedList(arr)
ll.printVal()
ll.deleteNode(4)
ll.printVal()

# things i learned: 
## 