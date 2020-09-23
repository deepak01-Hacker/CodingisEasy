#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given a Binary Tree of size N, you need to find all the possible paths from root node to all the leaf node's of the binary tree.

#Example :-
"""
Input:
       1
    /     \
   2       3

Output: 1 2 #1 3 #              <-

Explanation: 
    All possible paths:
    1->2
    1->3

"""


'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
def preorder(root,ans,arr):
    if root is None:
        return 
    arr.append(root.data)
    preorder(root.left,ans,arr)
    preorder(root.right,ans,arr)
    if root.left is None and root.right is None:
        ans.append([])
        for node in arr:
            ans[-1].append(node)
        arr.pop()
    else:
        if arr:
            arr.pop()
        
def Paths(root):
    ans = []
    preorder(root,ans,[])
    return ans

    

