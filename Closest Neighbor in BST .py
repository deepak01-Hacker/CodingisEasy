#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a binary search tree and a number N. Your task is to complete the function findMaxforKey(), 
#           that find's the greatest number in the binary search tree that is less than or equal to N. Print 
#           the value of the element if it exists otherwise print -1.


#Example :- 
"""
                     5
                  /     \
                2        12
              /   \     /   \
            1      3   9     21
                            /   \
                          19     25



        Input : N = 24
        Output :result = 21
        (searching for 24 will be like-5->12->21)

        Input  : N = 4
        Output : result = 3
        (searching for 4 will be like-5->2->3)

"""


'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
def findMaxforKey(root,k):
    mins = -1
    while(root):
        if root.data <= k:
            mins = root.data
        if root.data <= k:
            root = root.right
        else :
            root = root.left
    print(mins)
