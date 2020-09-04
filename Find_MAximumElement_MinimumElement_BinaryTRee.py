#User function Template for python3
"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
"""
#Question-> Find Minimum and Maximum Element in Binary Tree

#Tags : Easy,Tree,GeeksForGeeks

#Constraints:
#1<=T<=10^5
#1<=n<=10^5
#1<=data of the node<=10^5




'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def findMax(curr):
    if curr is None:
        return -1
    return max(curr.data,findMax(curr.left),findMax(curr.right))
    
def findMin_(curr):
    if curr is None:
        return 10**5
    return min(curr.data,findMin_(curr.left),findMin_(curr.right))

    
def findMin(root):
    cur = root
    return findMin_(cur)

#Happy Coding ; )