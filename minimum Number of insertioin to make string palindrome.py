#Python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Minimum Numbers of Insertion to make string Palindrome.

#Example :-
"""
    Input :
        1
        abd
    Output :
        2
    Explanation :
        Here abd is String so if we insert db in abd so dbabd so it is convert into palindrome in 2 insertion :)
"""


def makeStringPalindrome(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return len_string1 - dp[len_string1][len_string2]

if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        print(makeStringPalindrome(string,string[::-1],len(string),len(string)))
