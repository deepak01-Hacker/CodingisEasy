#python3
"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

    Que-> Given a Binary Tree of size N , where each node can have positive 
    or negative values. Convert this to a tree where each node contains the 
    sum of the left and right sub trees of the original tree. The values of 
    leaf nodes are changed to 0.
"""

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def inorder(root):
    if root is None :
        return 0
    elif (root.left is None and root.right is None):
        t = root.data
        root.data = 0
        return t
    k = root.data
    root.data = inorder(root.left)+inorder(root.right)
    return root.data + k
    
def toSumTree(root):
    inorder(root)