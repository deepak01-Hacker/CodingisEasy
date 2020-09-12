#Python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem : Coin Change Problem : Minimum number of ways to get sum 


def minimumWays(arr,sum_):

    dp = [[0 for _ in range(sum_+1)]for _ in range(len(arr)+1)]

    for i in range(len(arr)+1):
        for j in range(sum_+1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = 10**6
            elif i == 1:
                if sum_%arr[i-1] == 0:
                    dp[i][j] = sum_//arr[i-1]
            elif arr[i-1] <= j:
                dp[i][j] = min(dp[i][j-arr[i-1]] + 1,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[len(arr)][sum_])

if __name__ == "__main__":
    for _ in range(int(input())):
        sum_ = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        minimumWays(arr,sum_)