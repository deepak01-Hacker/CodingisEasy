#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem :- Given a special Binary Tree whose leaf nodes are connected to form a circular doubly linked list. 
#           Find the height of this special Binary Tree.

#Example:
"""
        Input:
          1
        /   \
       2     3
     /
    4
    Output: 3
    Explanation: There are 3 edges and 4
        nodes in spiral tree where leaf nodes
        4 and 3 are connected in circular
        doubly linked list form. Thus the
        height of spiral tree is 3.

"""

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return the height of the given special binary tree


def hight(root):
    if root is None :
        return 0;
    l = hight(root.left)
    r = hight(root.right)
    if l>r:
        return l+1
    else:
        return r+1

def findTreeHeight(root):
    s = set()
    stack = []
    level = 1
    stack.append(root)
    flag = False
    Root = None
    while(True):
        le = len(stack)
        if le:
            level += 1
            while(le):
                curr = stack.pop(0)
                if curr in s:
                    flag = True
                    Root = curr
                    break
                s.add(curr)
                if curr.left :
                    stack.append(curr.left)
                if curr.right :
                    stack.append(curr.right)
                le -= 1
            if flag :
                break
        else:
            break
    gt = Root
    while(gt):
        prev = gt.right
        curr = gt
        curr.left = None
        curr.right = None
        gt = prev
    return hight(root)
    
    
