#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#$Tags :- Dynamic Programming, Matrix Chain Multiplication ,String , List , InterviewPrepration ,DP-17,Memoization 

#Problem :- Given a string, a partitioning of the string is a palindrome partitioning if every substring 
#           of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of 
#           “ababbbabbababa”. Determine the fewest cuts needed for a palindrome partitioning of a given string. 
#           For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”. 
#           If a string is a palindrome, then minimum 0 cuts are needed. If a string of length n containing all 
#           different characters, then minimum n-1 cuts are needed.


"""
Examples :

    Input : str = “geek”
    Output : 2
    We need to make minimum 2 cuts, i.e., “g ee k”

    Input : str = “aaaa”
    Output : 0
    The string is already a palindrome.

    Input : str = “abcde”
    Output : 4
"""

import sys

dp = [[0 for _ in range(1001)] for _ in range(1001)]

def isPalindrome(st,start,end):
    ans = list(st)
    check = ans[start:end+1]
    return check == check[::-1]

def palindromePartition(st,i,j):
    global dp
    if i>=j:
        return 0
    if isPalindrome(st,i,j):
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    mini = sys.maxsize
    for k in range(i,j):
        temp = (palindromePartition(st,i,k)+palindromePartition(st,k+1,j))+1
        mini = min(temp,mini)
    dp[i][j] = mini
    return dp[i][j]

if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        for i in range(len(string)+1):
            for j in range(len(string)+1):
                dp[i][j] = 0
        print(palindromePartition(string,0,len(string)-1))