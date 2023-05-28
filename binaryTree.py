class BTreeNode:
    def __init__ (self,number):
        self.data=number
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.data) + " - "
    
    def add(self,newNumber):
        if (self is not None):
            if (newNumber < self.data):
                if (self.left is None):
                    self.left=BTreeNode(newNumber)
                else:
                    self.left.add(newNumber)
            
            else: #if newNumber >= self.data
                if (self.right is None):
                    self.right=BTreeNode(newNumber)
                else:
                    self.right.add(newNumber)

    def printTree(self):
        #print(self,end="") #preOrder traversing
        if (self.left is not None):
            self.left.printTree()
        print(self,end="") #inOrder traversing
        if (self.right is not None):
            self.right.printTree()
        #print(self,end="") #postOrder traversing

root=BTreeNode(47)

root.add(25)
root.add(43)
root.add(77)
root.add(65)
root.add(68)
root.add(93)
root.add(11)
root.add(17)
root.add(44)
root.add(31)
root.add(7)

root.printTree()