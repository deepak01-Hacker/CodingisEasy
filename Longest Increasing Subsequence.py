#Python3

""" 
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Find the longest increasing subsequence in Given Array .
$TaGs : Dynamic Programming , LIS , Array


#Example :-
"""
    Input : 
        1
        6
        5 1 2 7 3 9
    Output :   
        4
"""


def LIS(arr,n):

    dp = [0]*n
    dp[0] = 1

    for i in range(1,n):
        dp[i] = 1
        for j in range(0,i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = 1+dp[j]
    return max(dp)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(LIS(arr,n))