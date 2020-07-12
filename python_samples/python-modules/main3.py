from karma.tree import BinaryTree,in_order

if __name__ == '__main__':
    r = BinaryTree('a',BinaryTree('b',BinaryTree('c', None, None), None),BinaryTree('e',None,BinaryTree('f',None,None)))
    in_order(r)
