#Python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
"""

#Problem : Convert Binary Tree into Binary Search Tree

#Hint : Trverse array inorder and append element in array and sort it and after that corrosponding to array set Tree Node Values.
# 


'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def inorder(root,arr):
    if root is None:
        return 
    else:
        BST(root.left,arr)
        arr.append(root.data)
        BST(root.right,arr)
        
def settotree(root,arr):
    if root is None:
        return
    else:
        settotree(root.left,arr)
        root.data = arr[0]
        arr.pop(0)
        settotree(root.right,arr)
        
def binaryTreeToBST(root):
    arr = []
    set_= Send_ = root
    BST(set_,arr)
    arr.sort()
    settotree(root,arr)
    return send_

#HAppy Coding Its a Really a magic Algorithm so ,,,,,,,,,,,,,,,,,,,,,,,, keep doing coding ; )
