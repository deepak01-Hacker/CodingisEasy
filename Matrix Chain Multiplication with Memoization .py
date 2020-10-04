#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
#           The problem is not actually to perform the multiplications, but merely to decide in which order 
#           to perform the multiplications.

#Example :- 
"""
    Input: p[] = {40, 20, 30, 10, 30}   
    Output: 26000  
    There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
    Input: p[] = {40, 20, 30, 10, 30}   
    Output: 26000  
    There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
    Let the input 4 matrices be A, B, C and D.  The minimum number of 
    multiplications are obtained by putting parenthesis in following way
    (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

    Input: p[] = {10, 20, 30, 40, 30} 
    Output: 30000 
    There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
    Let the input 4 matrices be A, B, C and D.  The minimum number of 
    multiplications are obtained by putting parenthesis in following way
    ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

    Input: p[] = {10, 20, 30}  
    Output: 6000  
    There are only two matrices of dimensions 10x20 and 20x30. So there 
    is only one way to multiply the matrices, cost of which is 10*20*30

"""

import sys



dp = [[0 for _ in range(1001)] for _ in range(1001)]


def matrixChainMultiplication(arr,i,j):
    global dp
    if i>=j:
        return 0;
    if dp[i][j] != 0:
        return dp[i][j]
    _mini = sys.maxsize
    for k in range(i,j):
        temp = matrixChainMultiplication(arr,i,k)+matrixChainMultiplication(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        _mini = min(_mini,temp)
    dp[i][j] = _mini
    return dp[i][j]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        for i in range(n+1):
            for j in range(n+1):
                dp[i][j] = 0
        print(matrixChainMultiplication(arr,1,n-1))