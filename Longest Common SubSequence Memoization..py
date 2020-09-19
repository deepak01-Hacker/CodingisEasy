#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem :- Find the maximum Longest Common Subsequence in Given Two String :?
#TaGs : Dynamic Programming  , Memoization , Improve some Complexity

#Explanation :-
"""
    string 1 : abscjfdojs
    string 2 : kjfanabsc

    Output : 4
"""

dp = [[0 for _ in range(1001)] for _ in range(1001)]

def LCS(lengthStringFirst,lengthStringSecond,st1,st2):
    global dp
    if lengthStringFirst == 0 or lengthStringSecond == 0:
        return 0
    if dp[lengthStringFirst][lengthStringSecond]:
        return dp[lengthStringFirst][lengthStringSecond]
    if st1[lengthStringFirst-1] == st2[lengthStringSecond-1]:
        dp[lengthStringFirst][lengthStringSecond] = 1+LCS(lengthStringFirst-1,lengthStringSecond-1,st1,st2)
        return dp[lengthStringFirst][lengthStringSecond]
    else:
        dp[lengthStringFirst][lengthStringSecond] = max(LCS(lengthStringFirst,lengthStringSecond-1,st1,st2),LCS(lengthStringFirst-1,lengthStringSecond,st1,st2))
        return dp[lengthStringFirst][lengthStringSecond]

if __name__ == "__main__":
    for _ in range(int(input())):
        String1 = input()
        String2 = input()
        print(LCS(len(String1),len(String2),String1,String2))#Function that REturns Longest Common Subsequence length ////
