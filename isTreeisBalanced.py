#User function Template for python3

"""
    Code By    : Deepak Kumar(Insan)
    Contact us : a9649060356@gmail.com

"""

#Problem -: Check Tree is Balanced Or not :)

#Tags : Easy , Tree ,GeeksForGeeks

'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''

def hight(curr_root):
    if curr_root is None:
        return 0
    else:
        return 1+max(hight(curr_root.left),hight(curr_root.right))
        
def isBalanced(root):
    if root is None:
        return True
    elif root:
        l = hight(root.left)
        r = hight(root.right)
        if abs(l-r) > 1:
            return False
        else:
            return isBalanced(root.left) and isBalanced(root.right)

