#Python3

"""
    Code By   : Deepak Kumar
    Contat Us : a9649060356@gmail.com

"""

#Problem :- Given a BST and a value x, the task is to delete the nodes having values greater than or equal to x.

#Example:
"""
    Input:
        2
        7
        20 8 22 4 12 10 14
        8
        7
        20 8 22 4 12 10 14
        10
    Output:
        4
        4 8
"""




def deleteNode(root, x):
    if root is None:
        return
    if root.data >= x:
        root = deleteNode(root.left,x)
        return root
    else:
        root.right = deleteNode(root.right,x)
        return root



class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def deleteNode(root, x):
    curr = root
    stack = []
    main_root = None
    while(True):
        if curr:
            stack.append(curr)
            curr = curr.left
        elif (stack):
            curr = stack.pop()
            if curr.data >= x:
                main_root = curr.left
                break
            if curr.left and curr.left.data >= x:
                curr.left = None
            if curr.right and curr.right.data >= x:
                curr.right = None
            curr = curr.right
        else:
            break
    if main_root:
        return main_root
    return root
    

