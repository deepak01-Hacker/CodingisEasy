#User function Template for python3
"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""
#Problem :- Given a Binary Tree of N nodes. Find the vertical width of the tree.
#TaGs    :  Easy , Tree, GeeksForGeeks,Recursion , Map
#
# Example :-
 """
    Input:
          1
       /    \
      2      3
     / \    / \
    4   5  6   7
            \   \
             8   9
Output: 6
Explanation: The width of a binary tree is
the number of vertical paths in that tree.

Go on the Question : https://practice.geeksforgeeks.org/problems/vertical-width-of-a-binary-tree/1/?category[]=Tree&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]TreeproblemStatusunsolveddifficulty[]0page1

The above tree contains 6 vertical lines.
 """ 


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def inorder(root,level,map):
    if root is None:
        return 
    inorder(root.left,level-1,map)
    map[level] = 1
    inorder(root.right,level+1,map)
    
    
def verticalWidth(root):
    if root is None:
        return 0
    map = {}
    inorder(root,0,map)
    return len(map)
    
    