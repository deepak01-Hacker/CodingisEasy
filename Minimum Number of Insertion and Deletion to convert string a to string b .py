#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
    If you have any Doubt related to this Question , You can mail me.

"""

#Problem :- Minimum Number of Insertion and Deletion to convert String A to String B .
#TaGs : LCS , Dynamic Programming 

#Example:-
"""
    Input : 
        string a : heap
        string b : pea
    Output : 
        3
"""

def LCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len_string1][len_string2]

def convertString(string1,string2):
    lengthOfLCS = LCS(string1,string2,len(string1),len(string2))
    print(len(string1)+len(string2)-(lengthOfLCS*2))          #Here We double the lengthOFLCS bcz this value is common in Both the String 

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        convertString(string1,string2)
