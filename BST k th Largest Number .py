#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem :- Given a Binary search tree. Your task is to complete the function which will return the Kth 
#           largest element without doing any modification in Binary Search Tree.

#Example :- 
"""
    Example 1:

    Input:
          4
        /   \
       2     9
    k = 2 
    Output: 4
"""




# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
def inorder(root,k,arr):
    global ans
    if root is None:
        return 
    inorder(root.right,k,arr)
    if len(arr) == k:
        return None
    arr.append(root.data)
    inorder(root.left,k,arr)
        
def kthLargest(root, k):
    arr = []
    inorder(root,k,arr)
    return arr[k-1]
