#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

$ Tags : Dynamic Programming , Array , Recursion ,Python 

#Problem :- The first line of input contains an integer T denoting the no of 
#           test cases . Then T test cases follow. Each test case contains 3 lines .
#           The first line of each test case is an integer N denoting the size of the array A. 
#           In the next line are N space separated values of the array A. In the next line is an 
#           integer x.

#Example : 

""" 
    Input:
        2
        7
        3 5 10 15 17 12 9
        4
        4
        5 15 10 300
        12
    Output:
        62
        25

"""


def pairSum(arr,curr,next,k):
    if curr < 0 or next < 0:
        return 0
    if abs(arr[curr] - arr[next]) < k:
        return arr[curr] + arr[next] + pairSum(arr,next-1,next-2,k)
    return max(pairSum(arr,curr,next-1,k),pairSum(arr,next,next-1,k))

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split()))
        k = int(input())
        print(pairSum(arr,n-1,n-2,k))