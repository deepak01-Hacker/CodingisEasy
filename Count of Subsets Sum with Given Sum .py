#python3
#Dp Knapsack Varient 
#Dynamic Programming 
"""
Code By : Deepak Kumar 
Contact us : a 9649060356@gmail.com
"""
#Question- > Count all Subsets in the array with given Sum


def coutsubsetTargetSum(arr,tr_s,length):

    dp = [[0 for _ in range(tr_s+1)] for _ in range(length+1)]

    for index in range(length+1):
        for sums_atpoint in range(tr_s+1):
            if sums_atpoint == 0:
                dp[index][sums_atpoint] = 1
            elif index == 0:
                dp[index][sums_atpoint] = 0
            elif arr[index-1] <= sums_atpoint:
                dp[index][sums_atpoint] = dp[index-1][sums_atpoint-arr[index-1]] + dp[index-1][sums_atpoint]
            else:
                dp[index][sums_atpoint] = dp[index-1][sums_atpoint]
    return dp[length][tr_s]

if __name__ == "__main__":
    for _ in range(int(input())):
        Target_sum = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(coutsubsetTargetSum(arr,Target_sum,len(arr)))

#codeing is easy with dp and Recursion