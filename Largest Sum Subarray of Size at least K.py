#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given an array and a number k, find the largest sum of the subarray containing at least k numbers. 
#           It may be assumed that the size of array is at-least k.


$TaGs : Array , Dynamic Programming , Window Sliding 

#Example :- 
"""
    Input:
        8
        -521 421 -843 450 -798 321 -120 53
        5

    output:
        -94

"""

def largestSum(arr,n,k):
    subA = []
    left = 0
    size = 0
    sum = 0
    for i in range(k):
        sum += arr[i]
    subA.append(sum)
    for right in range(k,n):
        sum += arr[right]
        sum -= arr[left]
        left += 1
        subA.append(sum)
    return subA

def res(arr,n,k):
    subA = largestSum(arr,n,k)
    sum = subA[0]
    left = 0
    maxs = subA[0]
    for i in range(k,n):
        sum += arr[i]
        if sum < subA[i-k+1]:
            sum = subA[i-k+1]
        maxs = max(maxs,sum)
    print(maxs)
        
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    k = int(input())
    res(arr,n,k)