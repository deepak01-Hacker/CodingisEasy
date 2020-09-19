#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Print Element of Tree that are In Given Range 

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# returns a list of node values in the BST (rooted at 'root')
# that lie in the given range [low, high]
def inorder(root,low ,high,arr):
    if root is None:
        return 
    inorder(root.left,low,high,arr)
    if root.data >= low and root.data <= high:
        arr.append(root.data)
    inorder(root.right,low,high,arr)
def printNearNodes(root, low, high):
    arr=[]
    inorder(root,low,high,arr)
    return arr
    

