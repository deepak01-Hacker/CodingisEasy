//#Java

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

//Problem : Given a Two Binary Trees, write a function that returns true if one is 
//         mirror of other, else returns false.

//#Explanation : 
"""
     Input:
T1:     1     T2:     1
      /   \         /   \
     2     3       3     2
Output: 1

"""

//#Code 


//Input:
/* A Binary Tree node
class Node
{
    int data;
    Node left, right;
   Node(int item)    {
        data = item;
        left = right = null;
    }
} */

class Tree {
    boolean areMirror(Node a, Node b) {
        if ((a == null) && (b == null)){
            return true;
        }
        if (a.data != b.data){
            return false;
        }
        else{
            return (areMirror(a.left,b.right) && areMirror(a.right,b.left));
        }
    }
}