#User function Template for python3
"""
    Code by: Deepak Kumar
    Contact us : a9649060356@gmail.com
"""
"""
Questioin - > Given a Binary Search Tree (with all values unique) and two node values.
              Find the Lowest Common Ancestors of the two nodes in the BST.
"""

#Tree EAsy Level Problem of GFG
#Hint : Apply Binary Search on Tree 


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def binarySearch(root,n1,n2):
    first_number = n1
    second_number = n2
    n1 = min(first_number,second_number)
    n2 = max(first_number,second_number)
    while(True):
        if root.data > n1 and root.data < n2:
            return root
        elif root.data == n1 or root.data == n2 :
            return root
        elif root.data < n1 and root.data < n2:
            root = root.right
        else:
            root = root.left
        
def LCA(root,n1,n2):
    return binarySearch(root,n1,n2)

#Happy Coding ;) 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Thanks for visiting on my Code :)

