#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- You are given array A of size n. You need to find the maximum-sum sub-array with the condition that 
#           you are allowed to skip at most one element.

#Example :-
"""
    Input:
        n = 5
        A[] = {1,2,3,-4,5}
    Output: 11
    Explanation: We can get maximum sum
    subarray by skipping -4.

"""


def maxSumSubarray(A, n):
    
    sum = A[0]
    max_ = A[0]
    skip =A[0]
    for i in range(1,n):
        temp =sum
        sum += A[i]
        sum = max(sum,A[i])
    
        skip = max(temp,skip+A[i])
    
        temp = max(sum,skip)
    
        max_ = max(temp,max_)
        print(sum,max_,skip)
    return max_

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(maxSumSubarray(arr,len(arr)))