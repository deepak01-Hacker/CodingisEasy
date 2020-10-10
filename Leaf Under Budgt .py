
#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a binary tree and a budget. Assume you are at the root of the tree(level 1), you need to maximise 
#           the count of leaf nodes you can visit in your budget if the cost of visiting a leaf node is equal to the 
#           level of that leaf node. Note : 1 base indexing for level


#Example :- 
"""
    Input:
        1
        6
        10 8 L 8 3 L 10 2 R 2 3 L 3 4 R 2 6 R
        8
        Output:
        2
        Explanation:
            TestCase 1:
            Binary Tree is as:
                  10
                /       \
              8         2
            /         /       \
          3        3         6
                       \
                        4  
            Cost For visiting Leaf Node 3: 3(level)
            Cost For visiting Leaf Node 4: 4(level)
            Cost For visiting Leaf Node 6: 3(level)
            In budget one can Max 2 Leaf Nodes.

"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def ans(root,stack,level):
    if root is None:
        return 
    if root.left is None and root.right is None:
        stack.append(level)
        return 
    ans(root.left,stack,level+1)
    ans(root.right,stack,level+1)
    
def getCount(root,budgt):
    stack = []
    ans(root,stack,1)
    stack.sort()
    count = 0
    for i in stack:
        if i<= budgt:
            count += 1
            budgt -= i
        else:
            break
    return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        budgt=int(input())
        #n1,n2=list(map(int,input().split()))
        
        print(getCount(tree.root,budgt))