#Python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given the binary Tree of and two-node values. Check whether the two-node values are cousins of each other or not.

#Example :-
"""
    Input:
          1
        /   \
       2     3
     a = 2, b = 3
    Output: 0
"""


def isCousinW(root, a, b):
    A_N = -1
    L_N = -10
    stack = []
    stack.append(root)
    level = 0
    flag = False
    while(True):
        length = len(stack)
        if length:
            level += 1
            while(length):
                curr = stack.pop(0)
                if (curr.left and (curr.left.data == a or curr.left.data == b)) and (curr.right and (curr.right.data == a or curr.right.data == b)):
            
                    A_N = -1
                    L_N = -10
                    flag = True
                    break
                if curr.data == a:
                    A_N = level
                elif curr.data == b:
                    L_N = level
                if curr.left :
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                length -= 1
            if flag :
                return False
        else:
            break
    if A_N == L_N :
        return True

    

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
""" #TEST
if __name__=="__main__":
    t=1
    for _ in range(0,1):
        s="1 2 3"
        root=buildTree(s)
        n1 = 2
        n2 = 3
        levelOrder(root)
        print(isCousinW(root,n1,n2))

        #ans=isCousin(root,n1,n2)
        """"
# } Driver Code Ends