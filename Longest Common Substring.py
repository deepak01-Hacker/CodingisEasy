#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#TaGs : Dynamic Programming , LCS , String , GeeksForGeeks 

#Problem :- Given Two String , Find the maximum common Substring Length > ?

#Example:
"""
    Input : 
        1
        abscgfkjg
        kjfjgnjabs
    
    Output :      // The common substring is "abs"
        3
"""




def maxLengthCommonSubstring(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    ans = -1
    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
            ans = max(ans,dp[i][j])
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        maxLengthCommonSubstring(string1,string2,len(string1),len(string2))