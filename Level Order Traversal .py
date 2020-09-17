#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Find the Level Order Traversal Order ?
#TAGs : Tree ,Level - Order Traversal , Easy


"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

# Your task is to complete this function
# Function should return the level order of the tree in the form of a list of integers

def levelOrder(root):
    result = []
    stack = []
    stack.append(root)
    while(stack):
        curr = stack.pop(0)  #You can print Here curr.data 
        result.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return result

#Happy Coding ; )
    

