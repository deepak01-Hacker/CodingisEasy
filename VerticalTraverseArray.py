#python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem : Given a Binary Tree. Vertical  Traversal of the Binary Tree.

#TaGs : Easy , Tree , GeeksForGeeks

#Explantion : Print a Binary Tree in Vertical Order
"""
Input : 
          1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 
               
              
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

"""

def verticalOrder(root,vert_levl,map):
    if root is None:
        return 
    try :
        map[hd].append(root.data)
    except:
        map[hd] = [root.data]
    verticalOrder(root.left,vert_levl-1,map)
    verticalOrder(root.right,vert_levl+1,map)

def verticalTraverse(root):
    map = {}
    verticalOrder(root,0,map)
    for i in sorted(map):
        for value in map[i]:
            print(value,end=" ")
        print()
    