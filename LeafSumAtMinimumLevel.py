#User function Template for python3


"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem :- Given a Binary Tree of size N, your task is to complete the function minLeafSum(), 
#           that should return the sum of all the leaf nodes that are at minimum level of the given binary tree.

#Tags : Easy , Tree, GeeksForGeeks

#Explanation :- 
"""
    Input : 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
  /  \ 
 7    2      

Output :
    sum = 5 + 8 = 13
"""



'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

def minLeafSum(root):
    stack = []
    stack.append(root)
    sum = 0
    while(True):
        length = len(stack)
        if length > 0:
            while(length):
                curr = stack.pop(0)
                if curr is None:
                    break
                if curr.left != None:
                    stack.append(curr.left)
                if curr.right != None:
                    stack.append(curr.right)
                if curr.left is None and curr.right is None:
                    sum += curr.data
                length -= 1
            if sum >0:
                return sum
        else:
            break
    return sum
    
