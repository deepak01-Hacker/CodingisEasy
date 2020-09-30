#Python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), 
#           that find the sum of all nodes on the longest path from root to leaf node.
#           If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

#Example:
"""
    Input : Binary Tree

        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6           
    

    Output : 13

         4        
      //   \       
      2     5      
     / \\  / \     
    7  1  2  3 
      //
     6

The highlighted nodes (4, 2, 1, 6) above are 
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13

     
     
      """


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


#User function Template for python3


def pre(root,arr):
    if root is None:
        return None
    pre(root.left,arr)
    pre(root.right,arr)
    if root.left and root.left == arr[-1]:
        arr.append(root)
    elif root.right and root.right == arr[-1]:
        arr.append(root)


def ino(root):
    stack = []
    stack.append(root)
    matrix = []
    while(True):
        len_ = len(stack)
        if len_:
            matrix = []
            while(len_):
                curr = stack.pop(0)
                if curr:
                    matrix.append(curr)
                if curr and curr.left:
                    stack.append(curr.left)
                if curr and curr.right:
                    stack.append(curr.right)
                len_ -= 1
        else:
            break
    maxs = 0
    for i in matrix:
        arr = []
        arr.append(i)
        pre(root,arr)
        t = 0
        for node in arr:
            t += node.data
        maxs = max(maxs,t)
    return maxs

    
def sumOfLongRootToLeafPath(root):
    return ino(root)