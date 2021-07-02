## Day 6 07/01/21

## Question: Return true if the two bst are the same.
class node:
    def __init__(self,x) -> None:
        self.val = x
        self.left = None
        self.right = None
    def setLeft(self,leftNode):
        self.left = leftNode
    def setRight(self,rightNode):
        self.right = rightNode
    

def ifBSTsame(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return ifBSTsame(p.left,q.left) and ifBSTsame(p.right,q.right)

rootp = node(5)
rootp.setLeft(node(1))
rootp.setRight(node(10))

rootq = node(5)
rootq.setLeft(node(1))
rootq.setRight(node(10))


print(ifBSTsame(rootp,rootq))

## Things we learned:
## 1. For tree questions, better think of recurtion first, bc you don't know how deep the tree is, so iteration sometime is hard for trees.
## 2. For recurtion, the order of base cases are matters. For example, I can't change the order of two base case bc when both of q and p are none, and if they go into line18 one first,
##    it will return false which is wrong.
## 3. A function should ONLY RETURN ONE TYPE OF THING!!!! boolean return boolean, number return number.