#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem : Minimum Number of Deletion To make String Palindrome.
#TaGS : Dynamic Programming , LCS , Array , String


#Example:-
"""
    Input : 
        string a : heap
    Output : 
        3

"""
def LCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string1+1)] for _ in range(len_string2+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[len_string1][len_string2]

def MinimumdeletionPalindrome(string1,len_string1):
    return len_string1 - LCS(string1,string1[::-1],len_string1,len_string1)

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        print(MinimumdeletionPalindrome(string1,len(string1)))