#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given an array of integers A. A subsequence of A is called Bitonic if it is first increasing then decreasing.
$TaGs : Dynamic Programming ,Array, Longest increasing sequence 


#Example :-
"""
    Example:
        Input:
            2
            6
            80 60 30 40 20 10
            9
            1 15 51 45 33 100 12 18 9

        Output:
            210
            194

    Explanation:
        Testcase2:
            Input : A[] = {1, 15, 51, 45, 33, 100, 12, 18, 9}
            Output : 194
            Bi-tonic Sub-sequence are :
            {1, 51, 9}
            {1, 50, 100, 18, 9}
            {1, 15, 51, 100, 18, 9}
            {1, 15, 45, 100, 12, 9}
            {1, 15, 45, 100, 18, 9} .. so on           
            Maximum sum Bi-tonic sub-sequence is 1 + 15 + 51 + 100 + 18 + 9 = 194  

"""


def LIS(arr,n):

    dp = [0]*n
    dp[0] = arr[0]

    for i in range(1,n):
        dp[i] = arr[i]
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],arr[i]+dp[j])
    return dp

if __name__=="__main__":
    for _m in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        res1 = LIS(arr,n)
        res2 = LIS(arr[::-1],n) 
        maxs = -10**5
        for i in range(n):
            maxs = max(maxs,res1[i]+res2[n-i-1]-arr[i])
        print(maxs)    
