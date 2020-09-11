#User function Template for python3


"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :-> Check the Give Binary Tree is BST if yes then return 1 or return 0

#Tags : GeeksForGeeks , BinarySearch Tree ,inorder Medium
#Hint : really My approach is very different But its deap idiology so Follow my Code :

#Explanation :
"""
    Input:
      2
    /    \
    1      3

    Output: 1
"""


'''
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
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)

def isBST(root):
    arr = []
    inorder(root,arr)
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return 0
    return 1
            

#Happy Coding ; )