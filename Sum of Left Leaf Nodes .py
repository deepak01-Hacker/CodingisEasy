#User function Template for python3


"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a Binary Tree of size N. Find the sum of all the leaf 
#           nodes that are left child of their parent of the given binary tree.

#Explanation : 
"""

    Input:
       1
     /   \
    2     3
Output: 2


"""
#Tags : Easy , Tree , Treversal , GeeksForGeeks

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
def include(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.data
    else:
        return 0
def ans(root):
    if root is None:
        return 0
    return ans(root.left)+ans(root.right)+include(root.left)
    
    
def leftLeavesSum(root_node):
    return ans(root_node)

