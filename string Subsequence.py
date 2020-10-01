#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem :- Given two strings S1 and S2, find the number of times the second string occurs in the first string, 
#           whether continuous or discontinuous.

#Example :-
""" 
    Input: 
        S1 = geeksforgeeks
        S2 = gks
    Output: 4
    Explaination: 
        For the first 'g' there 
        are 3 ways and for the second 'g' there 
        is one way. Total 4 ways.
"""

#Recursive Solution
def LCSR(string1,string2,_string1,_string2):
    if (_string1==0 and _string2 == 0 ) or _string2 == 0:
        return 1
    if _string1 == 0:
        return 0
    
    if string1[_string1-1] == string2[_string2-1]:
        return LCSR(string1,string2,_string1-1,_string2-1) + LCSR(string1,string2,_string1-1,_string2)
    return LCSR(string1,string2,_string1-1,_string2)


#Dynamic Programming SLn
def LCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if j == 0 :
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len_string1][len_string2]


if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        print(LCS(string1,string2,len(string1),len(string2)))