#User function Template for python3
"""
    Code By    : Deepak Kumar(Insan)
    Contact us : a9649060356@gmail.com
"""

#TaGs : GeeksForGeeks,Tree,Mind,Easy

#Problem :- Given a Binary Tree, find diameter of it.The diameter of a tree is 
#           the number of nodes on the longest path between two leaves in the tree. 
#           The diagram below shows two trees each with diameter nine, the leaves that 
#           form the ends of a longest path are shaded (note that there is more than 
#           one path in each tree of length nine, but no path longer than nine nodes).





def maxDepth(node,arr): 
    if node is None: 
        return 0 ;  
  
    else : 
        lDepth = maxDepth(node.left,arr)
        rDepth = maxDepth(node.right,arr)
        
        arr[0] = max(arr[0],(lDepth+rDepth+1))
        return 1+max(lDepth,rDepth)
    
def diameter(root):
    arr = [0]
    maxDepth(root,arr)
    return arr[0]
    












#//////////////////////////////// this is very wrost Case O(n**2)//////////////////////////////////////

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
    
def diameter(root):
    max_ = 0
    st = []
    st.append(root)
    while(st):
        curr = st.pop(0)
        l = maxDepth(curr.left)
        r = maxDepth(curr.right)
        if l+r > max_:
            max_ = l+r
        if curr.left :
            st.append(curr.left)
        if curr.right:
            st.append(curr.right)
    return max_+1
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
import sys
sys.setrecursionlimit(50000)
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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k=diameter(root)
        print(k)



# } Driver Code Ends