#User function Template for python3


"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Check The Given Binary Tree is Heap ? If yes then REturn True else return False
#Tags :- Heap , Tree ,Easy , GeeksForGeeks

#Hint : Heap have a Property that any root data in heap is always greater from its left subarray and right subarray node data's. Apply it ; )


#Explanation :
"""
    Input:
      3
    /    \
   1      2

    Output: 1
"""


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


#Your Function Should return True/False or 1/0
def checkLesser(root,val):
    if root is None:
        return True
    if root.data < val:
        return checkLesser(root.left,val) and checkLesser(root.right,val)
    else:
        return False
def inorder(root):
    if root is None:
        return True
    else:
        if inorder(root.left) and inorder(root.right) and checkLesser(root.left,root.data) and checkLesser(root.right,root.data):
            return True
        else:
            return False
def isHeap(root):
    return inorder(root)
    

#Happy Coding :)
    