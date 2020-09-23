#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Print Longest Common subsequence in Given Two String >
#TaGS : Dynamic Programming , LCS 

#Example : 
"""
    string 1 : abscjfdojs
    string 2 : kjfanabsc

    Output : absc
"""


def printLCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    start_ = len_string1
    last_ = len_string2
    ans = ""
    while(start_>0 and last_>0):
        if string1[start_-1] == string2[last_-1]:
            t = string1[start_-1]
            t += ans
            ans = t
            start_-=1
            last_-=1
        elif dp[start_-1][last_] > dp[start_][last_-1]:
            start_ -= 1
        else:
            last_ -= 1
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        printLCS(string1,string2,len(string1),len(string2))

#Happy Coding ;)