class BinaryTree:
    def __init__(self,v,l,r):
        self.value = v
        self.left = l
        self.right = r
        
    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
def in_order(tree):
    if(tree.getLeft() != None):
        in_order(tree.getLeft())
        
    print('['+tree.getValue()+']',end='')
    
    if(tree.getRight() != None):
        in_order(tree.getRight())
