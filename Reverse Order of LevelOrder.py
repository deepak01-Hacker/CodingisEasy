#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level. 

#Example :- 
"""
    Input :
        1
      /   \
     3     2

    Output: 3 2 1
    Explanation:
        Traversing level 1 : 3 2
        Traversing level 0 : 1

"""



'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    result = []
    stack = []
    stack.append(root)
    while(True):
        length = len(stack)
        if length:
            index = 0
            while(length):
                curr = stack.pop(0)
                result.insert(index,curr.data)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                length -= 1
                index += 1
        else:
            break
    return result
