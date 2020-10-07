#Python3 

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""
#Problem :- Given a binary tree and a number K, the task is to find sum of tree nodes at level k. 
#           The Binary Tree s given in string form: (node-value(left-subtree)(right-subtree)).

#Note : 0 Base Indexing in Tree

#Example :-
""" 
    Input:
        1
        2 
        (0(5(6()())(4()(9()())))(7(1()())(3()())))
    Output: 
        14
    Explaination:
    The Tree from the above String will formed as:
                             0
                          /     \
                       5         7
                    /      \     /    \
                   6       4    1     3
                             \
                             9 


"""


def kLevelSum(st,level):
    stack = []
    map = {}
    ans = ""
    for i in range(len(st)):
        if st[i].isdigit():
            ans += st[i]
        elif st[i] == "(":
            if ans :
                try:
                    map[len(stack)].append(ans)
                except:
                    map[len(stack)] = []
                    map[len(stack)].append(ans)
            stack.append("(")
            ans = ""
        else:
            ans = ""
            stack.pop()
    ans = 0
    for ele in map[level+1]:
        ans += int(ele)
    return ans 

if __name__ == "__main__":
   for _ in range(int(input())):
       level = int(input())
       Tree = input()
       print(kLevelSum(Tree,level))
