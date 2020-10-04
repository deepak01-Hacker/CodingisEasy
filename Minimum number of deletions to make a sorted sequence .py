#Python3

"""
    Code By : Deepak Kumar
    Contact Us : a9649060356@gmail.com
    
"""
#Problem :- Given an array arr of size N, the task is to remove or delete the minimum number of elements 
#           from the array so that when the remaining elements are placed in the same sequence order form 
#           an increasing sorted sequence.
$TaGs :- LIS(Longest increasing sequence) , Dynamic Programming , Array , Sorting

#Example :- 
"""
    Input: 
        N = 5, 
        arr[] = {5, 6, 1, 7, 4}
    Output: 2
    Explanation: Removing 1 and 4 leaves the 
                remaining sequence order as
                5 6 7 which is a sorted sequence.
"""

def minimumNumberOfDeletionToMakeSortedSequence(arr,n):

    dp = [0]*(n+1)

    dp[0] = 1
    for i in range(1,n):
        dp[i] = 1
        for j in range(0,i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = 1+dp[j]
    return n - max(dp)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(minimumNumberOfDeletionToMakeSortedSequence(arr,n))