#Python

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Find the Longest Palindrome SubSequence in Given String.
@TaGs : Dynamic Programming , LCS , String


#Example:
"""
    Input : 
        1
        GEEKSFORGEEKS
    Output:
        5
"""


def LCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[len_string1][len_string2]

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        print(LCS(string1,string1[::-1],len(string1),len(string1)))
        