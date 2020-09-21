#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""
#Problem :- Find the maximum Longest Common Subsequence in Given Two String :?

#TaGs : Dynamic Programming  , String,Top - Down

#Explanation :-
"""
    string 1 : abscjfdojs
    string 2 : kjfanabsc

    Output : 4
"""


def topDownDp(string1,string2,len_firstString,len_secondString):

    dp = [[0 for _ in range(len_secondString+1)] for _ in range(len_firstString+1)]

    for i in range(len_firstString+1):
        for j in range(len_secondString+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp[len_firstString][len_secondString])         #here the ANswer ; ) | \


if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        topDownDp(string1,string2,len(string1),len(string2))
    