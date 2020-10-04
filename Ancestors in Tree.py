#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""
#Problem :- Given a Binary Tree and a target key, you need to find all the ancestors of the given target key.

#Example :-
"""
Input :
              1
            /   \
          2      3
        /  \
      4     5
     /
    7
Key: 7

Ancestor: 4 2 1
"""

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def find(root,arr):
    if root is None:
        return 
    find(root.left,arr)
    find(root.right,arr)
    if root.left and root.left.data == arr[-1]:
        arr.append(root.data)
    elif root.right and root.right.data == arr[-1]:
        arr.append(root.data)
def Ancestors(root,target):
    arr = []
    arr.append(target)
    find(root,arr)
    arr.pop(0)
    return arr