#python3
""" 
Code By : Deepak kumar
Contact us : a9649060356@gmail.com

"""
#question - > find minium difference of sum of subsets 
#Dynamic problem 
#0/1 Knapsack VArient 


def minimumSubsetDifference(arr,range_,n):

    dp = [[False for _ in range(range_+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(range_+1): 
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif arr[i-1] <= j :
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    mins = range_
    for i in range(range_//2+1):
        print(dp[n][i],i)
        if dp[n][i]:
            if mins > abs(range_-i-i):
                mins = abs(range_-i-i)
    return mins
    
if __name__ == "__main__":
    for _ in range(int(input())):
        length_arr = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        range_ = sum(arr)
        print(minimumSubsetDifference(arr,range_,length_arr))
#happy coding