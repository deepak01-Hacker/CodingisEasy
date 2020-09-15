#python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem : Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

#TaGs : Easy , Tree , GeeksForGeeks

#Explantion : 
"""
   1. Input:
        3
      /   \
     2     1
    
    Output: 3 1 2
   
   2. Input:
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 
    
    Output: 7 9 7 8 8 6 9 10

"""

# return a list containing the zig zag level order traversal of the given tree
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def zigZagTraversal(root):
    stack = []
    stack.append(root)
    zig = True
    temp = []
    while(True):
        length = len(stack)
        if length :
            while(length):
                curr = stack.pop(0)
                temp.append(curr.data)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                length -= 1
            if zig:
                print(*temp,end =" ")
                zig = False
            else:
                print(*temp[::-1],end=" ")
                zig = True
            temp =[]
        else:
            break
    return temp
