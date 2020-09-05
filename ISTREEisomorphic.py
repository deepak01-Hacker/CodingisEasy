#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Question-> Find Both trees are Isomorphic ?


#Note : Isomorphic -> subtree of both trees are same means both tree are same 
#                     OR both trees Subtrees Left and right child are cross 
#                     Equal mean LeftchildofRoot1Subtree == RightchildofRoot2Subtree

#Tags : Easy , Tree , GeeksForGeeks

# Return True if the given trees are isomotphic. Else return False.
def inorder(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.data != root2.data :
        return False 
    else:
        return ((inorder(root1.left,root2.right) and inorder(root1.right,root2.left)) or (inorder(root1.left,root2.left) and inorder(root1.right,root2.right)))

def isIsomorphic(root1, root2): 
    return inorder(root1,root2)

#Happy Coding ;)
