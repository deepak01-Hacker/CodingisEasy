#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Check The First String Sequence is in String 2 if yes then return True else return False:
$TaGS : Dynamic Programming , LCS , String , Sequence Matching

#Example:
"""
    Input : 
        1
        aby
        akjjfdbjfjy
    Output :
        True
    Explanation :
        string 1 sequence is present in Second String
"""


def sequencePatterenMatching(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    if dp[len_string1][len_string2] == len_string1:
        return True
    return False

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()       #Main String
        string2 = input()       #Second String
        print(sequencePatterenMatching(string1,string2,len(string1),len(string2)))