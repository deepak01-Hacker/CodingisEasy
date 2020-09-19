#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given an array, write a program that prints 1 if array represents Inorder 
#           traversal of a BST, else prints 0. Note that all keys in BST must be unique.

#Explanation :-
"""
    Input:
        3
        5
        10 20 30 40 50
        6
        90 80 100 70 40 30
        3
        1 1 2

    Output
        1
        0
        0

"""


def checkArrayTraversalIsBST(arr,n):
    for i in range(1,n):
        if arr[i-1] >= arr[i]:
            return 0
    return 1
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    print(checkArrayTraversalIsBST(arr,n))