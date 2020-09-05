#python3
#Dynamic Programming


"""
    Code By     : Deepak Kumar(Insan)
    Contact us  : a9649060356@gmail.com

"""
#Tags : Dyanamic Programming , UnBounded KnapSack \\// In this Tags Section We are RElate this Problem To with previous Problem

#Question -> Find maximum Profit for cutting A Rod ? 
#            The REal Question is that Accourding to price array 
#            how cut the rod and get maximum Profit ?


def maximuProfit(length_Rod,length_arr,price_arr):

    dp = [[0 for _ in range(length_Rod+1)]for _ in range(len(price_arr)+1)]

    for i in range(1,len(price_arr)+1):
        for j in range(1,length_Rod+1):
            if length_arr[i-1] <= j:
                dp[i][j] = max(price_arr[i-1]+dp[i][j-length_arr[i-1]],dp[i-1][j])
                #print(dp[i][j-length_arr[i-1]],j-length_arr[i-1],i,j)
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[len(price_arr)][length_Rod])


if __name__ == "__main__":
    for _ in range(int(input())):
        length_Rod = int(input())
        length_arr = list(map(int,input().rstrip().split(" ")))
        price_arr = list(map(int,input().rstrip().split(" ")))
        maximuProfit(length_Rod,length_arr,price_arr)


