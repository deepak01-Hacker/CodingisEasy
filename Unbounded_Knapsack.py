#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
    Special Thanks to Amit Verma(From Youtube)
"""
#Ques-> If you have a Unbounded Knapsack then Calculate maximum Profit from value

#Dyanmic Programming : ) 

#very Simple approach 


def maximumProfit(wt,val,weight_t):

    dp = [[0 for _ in range(weight_t+1)]for _ in range(len(val))]

    for i in range(1,len(val)+1):
        for j in range(1,weight_t+1):
            if wt[i-1] < j:
                dp[i][j] = max(val[i-1]+dp[i][weight_t-j],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[len(arr)][weight_t])

if __name__ == "__main__":
    for _ in range(int(input())):
        wight_arr = list(map(int,input().rstrip().split(" ")))
        value_arr = list(map(int,input().rstrip().split(" ")))
        knapSackWight = int(input())
        maximumProfit(wight_arr,value_arr,knapSackWight)

#Happy coding 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------