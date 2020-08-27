#DYnamic Programming
"By Deepak Kumar"
"Contact us: a9649060356@gmail.com"

##Question Explanation
""" In this File We have write solution of Target sum in subset of array 
EX . arr = [2,3,5,9]
     sum is = 8 
     so this Code return TRue 
     bcz this array subset [3,5] sum is 8 .
     
     """
#Hint USE top down approach of Dp 

def itContainsSum(t_sum,arr):

    #here we create a matrix
    dp = [[False for _ in range(t_sum+1)]for _ in range(len(arr)+1)]


    for i in range(len(arr)+1):
        for j in range(t_sum+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(arr)][t_sum]

if __name__ == "__main__":
    for _ in range(int(input())):
        target_sum = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(itContainsSum(target_sum,arr))