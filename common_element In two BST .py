#User function Template for python3


#User function Template for python3
"""
    Code By    : Deepak Kumar(Insan)
    Contact us : a9649060356@gmail.com
"""

#TaGs : GeeksForGeeks,Tree,Mind,Easy
#Problem :- Given two Binary Search Trees(without duplicates). 
#           Find need to print the common nodes in them. In other words, 
#           find intersection of two BSTs


#Explantion : 
"""
   Input:
BST1:
                  5
               /     \
             1        10
           /   \      /
          0     4    7
                      \
                       9
BST2:
                10 
              /    \
             7     20
           /   \ 
          4     9

Output: 4 7 9 10


"""

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def AddElementIncommon_set(root,common_set):
    if root is None:
        return 
    AddElementIncommon_set(root.left,common_set)
    AddElementIncommon_set(root.right,common_set)
    common_set.add(root.data)
    
def FindCommonelemnt(root,common_set,result):
    if root is None:
        return 
    FindCommonelemnt(root.left,common_set,result)
    if root.data in common_set:
        result.append(root.data)
    FindCommonelemnt(root.right,common_set,result)
    
def printCommon(root1, root2):
    common_set = set()
    result = []
    AddElementIncommon_set(root1,common_set)
    FindCommonelemnt(root2,common_set,result)
    return result
