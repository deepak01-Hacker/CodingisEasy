#User function Template for python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com

"""
#Problem :->> Given a Binary Tree, find the maximum width of it. 
#             Maximum width is defined as the maximum number of nodes in any level.
#             For example, maximum width of following tree is 4 as there are 4 nodes at 3rd level.
"""
        1
       /     \
     2        3
   /    \    /    \
  4    5   6    7                  the maximum width is 4
    \
      8
"""


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def getMaxWidth(root):
    stack = []
    stack.append(root)
    max_width = 0
    while(True):
        length = len(stack)
        max_width = max(length,max_width)
        if length:
            while(length):
                curr = stack.pop(0)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                length -= 1
        else:
            break
    return max_width

#Happy Coding : ) 