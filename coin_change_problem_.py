#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#TaGs : Dynamic Programming , unbounded - Knapsack


#Problem : you have Given a Coin array and a other Coin now you have to do change this 
#          coin accourding array's element. Now find the ways of changing this sum.
#          In simply you have to convert Main coin into chain .
# 
# Note : You can repeate the arraycoin(array element)

#Explanation : coins = [1,2,3]
#              GivenCoin = 5
#              now the possible way to change this GivenCoin in this coins is 5
#              like 1+1+1+1+1 = 5 so this way += 1
#              like 1+1+1+2 = 5 ; way += 1 and so on ..............................


def wayofChanges(givenCoin,coins):

    dp = [[0 for _ in range(givenCoin+1)] for _ in range(len(coins)+1)]

    for index in range(len(coins)+1):
        for coinAtpoint in range(givenCoin+1):
            if coinAtpoint== 0:
                dp[index][coinAtpoint] = 1   ##1----------         
            elif index == 0:                            # ---- Is there ##1 and ##2 we have initialize dp[index][coinAtpoint] = 0 and 1
                dp[index][coinAtpoint] = 0   ##1----------      bcz if we have empty coin array then index == 0 is 0 and if j == 0 then the possiblity is 1
            elif coins[index-1] <= coinAtpoint:
                dp[index][coinAtpoint] = dp[index][coinAtpoint-coins[index-1]]+dp[index-1][coinAtpoint]
            else:
                dp[index][coinAtpoint] = dp[index-1][coinAtpoint]
    print(dp[len(coins)][givenCoin])

if __name__ == "__main__":
    for _ in range(int(input())):
        givenCoin = int(input())
        coins = list(map(int,input().rstrip().split(" ")))
        wayofChanges(givenCoin,coins)

#Happy Coding ;)