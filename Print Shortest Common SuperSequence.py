#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com 

"""

#Problem :- Print Shortest Common SuperSequence of Two Strings. You have to return string that contain all sequence of both strings
$TaGS : Dynamic Programming , Array , LCS(Longest Common SubSequence)

#Example :-
"""
    Input :
        1
        heap
        eap
    Output : 
        heap

"""

def SCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    st = ""
    i = len_string1
    j = len_string2
    while(i > 0 or j > 0):
        if string1[i-1] == string2[j-1]:
            st += string1[i-1]
            i -= 1
            j -= 1
        elif dp[i][j-1] > dp[i-1][j]:
            st += string2[j-1]
            j -= 1
        else:
            st += string1[i-1]
            i -= 1
    print(st[::-1])

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        SCS(string1,string2,len(string1),len(string2))