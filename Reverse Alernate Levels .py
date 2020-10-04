#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a complete binary tree, reverse the nodes present at alternate levels.

#Example :-
"""
    Input:
             1
          /   \
        3      2

Output:

             1
          /   \
        2      3

Explanation: Nodes at level 2 are reversed.

"""


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def preorder(root1, root2, lvl): 
    if (root1 == None or root2 == None): 
        return
  
    if (lvl % 2 == 0): 
        t = root1.data 
        root1.data = root2.data
        root2.data = t 
    preorder(root1.left, root2.right, lvl + 1) 
    preorder(root1.right, root2.left, lvl + 1) 
  
def reverseAlternate(root): 
    preorder(root.left, root.right, 0) 
