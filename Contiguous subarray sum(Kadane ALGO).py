#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
$TaGs : Dynamic Programming , Kadane Algorithm , Array , Medium , GeeksForGeeks

#Problem :- Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

#Example :
"""
    Input
        2
        5
        1 2 3 -2 5
        4
        -1 -2 -3 -4
    Output
        9
        -1

"""

def continoussubarraySum(arr,n):
    maxs = (-10**7)+1
    sum = 0
    for ele in arr:
        sum += ele
        if sum < ele:
            sum = ele
        maxs = max(maxs,sum)
    return maxs
    
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(continoussubarraySum(arr,n))