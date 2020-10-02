#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""
#Problem : Longest Increasing SubSequence with Recursion

#Explanation:
"""
    If you really want to learn DP and Recrsion then First Try Yourself :) 
"""


def LIS(arr,i,j):
    if i == 0 or j == 0:
        return 1
    if arr[j-1] <= arr[i-1]:
        return max(1+LIS(arr,i,j-1),LIS(arr,i-1,j-1))
    return LIS(arr,i,j-1)
    

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(LIS(arr,n,n-1))
