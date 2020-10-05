#User function Template for python3


"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- print Lowest Common Ancestor in Given Two Nodes :



class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


Ans = None
def pre(root,arr,s):
    if root is None:
        return ;
    pre(root.left,arr,s)
    pre(root.right,arr,s)
    if root.left and root.left.data == arr[-1]:
        arr.append(root.data)
        s.add(root.data)
    elif root.right and root.right.data == arr[-1]:
        arr.append(root.data)
        s.add(root.data)
        
def preA(root,arr,s):
    if root is None:
        return ;
    preA(root.left,arr,s)
    preA(root.right,arr,s)
    if root.left and root.left.data == arr[-1]:
        arr.append(root.data)

    elif root.right and root.right.data == arr[-1]:
        arr.append(root.data)
def An(arr,s):
    for i in arr:
        if i in s:
            return Node(i)
        
def lca(root, n1, n2):
    global Ans
    Ans = None
    s1 = set()
    arr = []
    arr.append(n1)
    root2 = root
    pre(root,arr,s1)
    arr = []
    arr.append(n2)
    s1.add(n1)
    preA(root2,arr,s1)
    return An(arr,s1)
    