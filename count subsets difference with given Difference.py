#python3
""" 
Code By : Deepak kumar
Contact us : a9649060356@gmail.com

"""
#question - > find minium difference of given difference 
#Dynamic problem 
#0/1 Knapsack VArient 


def minimumSubsetDifference(arr,range_,n):

    dp = [[0 for _ in range(range_+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(range_+1): 
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif arr[i-1] <= j :
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][range_]
if __name__ == "__main__":
    for _ in range(int(input())):
        length_arr = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        dif = int(input())
        range_ = (dif+sum(arr))//2 # here is Main logic : ) special thanks to AMit Verma
        print(minimumSubsetDifference(arr,range_,length_arr))
#happy coding