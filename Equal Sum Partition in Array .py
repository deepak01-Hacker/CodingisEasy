#Python3
"""
Date : Mon , Aug 24 11:36 PM

Code by : Deepak Kumar 
Contact us : a9649060356@gmail.com

"""

#Question: check can array divided into two parts according sum of array retur True or False
#Ex: arr = [5,5,1,11]
# ans = True
#Explanation : sum([5,5,1]) == sum([11])

#Dp Have many Similar Problem I you want to learn Dp then First learn many ALgos of DP after YOu practice and  think if you do with Honestly You learn Very fast DP .


def partitionValid(arr,sum,n):

    dp = [[ False for _ in range(sum+1)] for _ in range(n+1)]

    for i in range(n+1):        
        for j in range(sum+1):  
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif arr[i-1] <= j :
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        if sum(arr)%2 == 0: # if array's sum is Even then if and if only array equal subsets exist bcz array elements are integers so sum%2 != 0 is Not exist 
            print(partitionValid(arr,sum(arr)//2,n))
        else:
            print("False") # Bcz we find Odd = sum//2


#HAppy Coding :-)